from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
import traceback
import sys
import boto3
import ast
import json

def print_error():
    """Print the error message and exit script."""
    traceback.print_exc()
    print("Closing...")
    sys.exit()

class InstaBot:
    def __init__(self, target_username: str, chromedriver_path: str, name_aws_secret_insta: str) -> None:
        self.TARGET_USERNAME = target_username
        self.CHROMEDRIVER_PATH = chromedriver_path
        self.PUBLISHMENT_CLASS = "._aabd._aa8k._al3l"
        self.PUBLISHMENT_LINK_CLASS = ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk" + \
                                ".xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5" + \
                                ".x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd"
        self.IMAGE_CLASS = ".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3"
        self.LIKES_CLASS = ".x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"

        # GET INSTA USERNAME AND PASSWORD FROM AWS SECRETS MANAGER
        print(f"Getting Insta username and password from AWS Secrets Manager's secret '{name_aws_secret_insta}'...")
        try:
            secrets_manager = boto3.session.Session().client(service_name="secretsmanager", region_name="sa-east-1")
            secret_response_insta = secrets_manager.get_secret_value(SecretId=name_aws_secret_insta)
            self.INSTA_USERNAME = ast.literal_eval(secret_response_insta["SecretString"])["username"]
            self.INSTA_PASSWORD = ast.literal_eval(secret_response_insta["SecretString"])["password"]
                                    # ast.literal_eval() turns a string to a dict
            print("Insta username and password loaded.\n")
        except:
            print("Error getting secrets...\n")
            print_error()
        print("\n---------------------------------Object initialized successfully---------------------------------\n")

    def get_publishments_data(self):
        # INITIALIZING CHROME DRIVER
        print("Initializing Chrome driver...")
        try:
            # op = webdriver.ChromeOptions()
            # op.add_argument("headless") # don't open a Chrome window
            driver = webdriver.Chrome(executable_path=self.CHROMEDRIVER_PATH)#, options=op)
            print("Chrome driver initialized.\n")
        except:
            print("Error initializing Chrome driver...\n")
            print_error()
        
        # ENTER THE ACCOUNT
        print("   Entering the account...")
        try:
            driver.get("https://www.instagram.com/")
            time.sleep(4)
            login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            login.send_keys(self.INSTA_USERNAME) # fill username
            passw = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            passw.send_keys(self.INSTA_PASSWORD) # fill password
            time.sleep(0.5)
            passw.send_keys(Keys.ENTER) # press Enter
            time.sleep(10)
            print("    Login successfull.\n")
        except:
            print("    Login failed...\n")
            print_error()

        try:
            driver.get(f"https://www.instagram.com/{self.TARGET_USERNAME}/")
            time.sleep(3)
            posts = []
            publishments_obj = driver.find_elements(By.CSS_SELECTOR, self.PUBLISHMENT_CLASS)
            
            for p in publishments_obj:
                publish = p.find_element(By.CSS_SELECTOR, self.PUBLISHMENT_LINK_CLASS)
                publish_link = publish.get_attribute("href")
                publish.click()
                time.sleep(3)
                
                description = driver.find_element(By.CSS_SELECTOR, "._a9zs").find_element(By.TAG_NAME, "h1").text
                likes = driver.find_element(By.CSS_SELECTOR, self.LIKES_CLASS).text

                comments_obj = driver.find_elements(By.CSS_SELECTOR, "._a9ym")
                comments = []
                for c in comments_obj:
                    comments.append(c.find_element(By.CSS_SELECTOR, "._aacl._aaco._aacu._aacx._aad7._aade").text)


                body = {
                    "link": publish_link,
                    "description": description,
                    "likes": likes,
                    "comments": comments
                }
                posts.append(body)

                driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.ESCAPE)


            last_publishment = publishments_obj[-1].find_element(By.CSS_SELECTOR, self.IMAGE_CLASS)
            driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            #driver.execute_script("arguments[0].scrollIntoView(true);", publishments[-1]) # scroll down to last publishment showing on list
            time.sleep(1)
            
            # count = 0
            # while count < 150:
            #     time.sleep(1)
            #     new_last_publishment = driver.find_elements(By.CSS_SELECTOR, self.IMAGE_CLASS)[-1]
            #     driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            #     #driver.execute_script("arguments[0].scrollIntoView(true);", publishments[-1])

            #     if new_last_publishment == last_publishment:
            #         count += 1

            #     try:
            #         driver.find_element(By.CSS_SELECTOR, "._acan._acao._acas._aj1-").click() # button to try load more publishments again
            #         time.sleep(1)
            #         driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_UP)
            #         time.sleep(0.5)
            #         driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            #         count += 1
            #     except NoSuchElementException:
            #         pass

            #     last_publishment = new_last_publishment
            
            with open(f"{self.TARGET_USERNAME}.json", "w") as f:
                json.dump({"username": self.TARGET_USERNAME, "publishments": posts}, f)
            time.sleep(3000)
            driver.quit()
        except:
            print("Error.\n")
            print_error()
        