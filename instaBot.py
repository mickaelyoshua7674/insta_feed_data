from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import traceback
import sys
import boto3
import ast

def print_error():
    """Print the error message and exit script."""
    traceback.print_exc()
    print("Closing...")
    sys.exit()

class InstaBot:
    def __init__(self, target_username: str, chromedriver_path: str, name_aws_secret_insta: str) -> None:
        self.TARGET_USERNAME = target_username
        self.CHROMEDRIVER_PATH = chromedriver_path
        self.IMAGE_CLASS = ".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3"

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

        # INITIALIZING CHROME DRIVER
        print("Initializing Chrome driver...")
        try:
            op = webdriver.ChromeOptions()
            op.add_argument("headless") # don't open a Chrome window
            driver = webdriver.Chrome(executable_path=self.CHROMEDRIVER_PATH, options=op)
            print("Chrome driver initialized.\n")
        except:
            print("Error initializing Chrome driver...\n")
            print_error()

        # GET NUMBER OF PUBLISHMENTS
        print("Getting number of publishments...")
        try:
            driver.get(f"https://www.instagram.com/{self.TARGET_USERNAME}/")
            time.sleep(3)
            num_publishments = driver.find_elements(By.CSS_SELECTOR, "._ac2a")[0].text
            self.num_publishments = int(re.sub("(\.)|(,)", "", num_publishments)) # remove . or , from text and turning into a int
            driver.quit()
            print("Number of publishments loaded.\n")
        except:
            print("Error getting numbers...\n")
            print_error()
        driver.quit()
        print("\n---------------------------------Object initialized successfully---------------------------------\n")

    def scroll_down(self):
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

        print("Scrolling down...")
        try:
            driver.get(f"https://www.instagram.com/{self.TARGET_USERNAME}/")
            time.sleep(3)

            publishments = driver.find_elements(By.CSS_SELECTOR, self.IMAGE_CLASS)
            qtd_publishments = len(publishments)

            driver.execute_script("arguments[0].scrollIntoView(true);", publishments[-1]) # scroll down to last publishment showing on list
            time.sleep(1)

            while qtd_publishments < self.num_publishments:
                publishments = driver.find_elements(By.CSS_SELECTOR, self.IMAGE_CLASS)
                qtd_publishments = len(publishments)
                driver.execute_script("arguments[0].scrollIntoView(true);", publishments[-1])
            
            time.sleep(5)
            driver.quit()
        except:
            print("Error scrolling down.\n")
            print_error()
        