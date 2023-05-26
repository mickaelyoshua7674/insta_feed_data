from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import traceback
import sys
import boto3
import ast
import json
import re

def print_error():
    """Print the error message and exit script."""
    traceback.print_exc()
    print("Closing...")
    sys.exit()
    
def get_post_description(driver, DESCRIPTION_CLASS):
    try:
        description = driver.find_element(By.CSS_SELECTOR, DESCRIPTION_CLASS).find_element(By.TAG_NAME, "h1").text
    except NoSuchElementException:
        description = ""
    return description

def get_post_likes(driver, LIKES_CLASS, VIEWS_CLASS, PEOPLE_LIKED_CLASS, OTHER_PEOPLE_CLASS):
    try:
        t = driver.find_element(By.CSS_SELECTOR, LIKES_CLASS).text
        if re.search("like", t) or re.search("curti", t):
            likes = t
        else:
            liked_by_link = [i.get_attribute("href") for i in driver.find_elements(By.CSS_SELECTOR, OTHER_PEOPLE_CLASS) if re.search("liked_by", i.get_attribute("href"))][0]
            driver.get(liked_by_link)
            time.sleep(3)
            people = []
            people_liked_obj = driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS)
            for p in people_liked_obj:
                people.append(p)
            driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            time.sleep(2)

            count = 0
            while count < 10:
                new_people_liked_obj = driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS)
                for p in new_people_liked_obj:
                    if p not in people_liked_obj:
                        people.append(p)
                driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
                time.sleep(2)

                if people_liked_obj == new_people_liked_obj:
                    count += 1
                
                people_liked_obj = new_people_liked_obj
            
            likes = f"{len(people)} curtidas"

    except NoSuchElementException:
        driver.find_elements(By.CSS_SELECTOR, VIEWS_CLASS)[-1].click()
        time.sleep(1)
        likes = driver.find_element(By.CSS_SELECTOR, "._aauu").text
        
    except:
        print("Error getting likes / Views / Liked By.")
        print_error()

    return likes
    
def get_post_comments(driver, COMMENTS_CLASS, COMMENT_CLASS):
    try:
        comments_obj = driver.find_elements(By.CSS_SELECTOR, COMMENTS_CLASS)
        comments = []
        for c in comments_obj:
            comments.append(c.find_element(By.CSS_SELECTOR, COMMENT_CLASS).text)
    except NoSuchElementException:
        comments = []
    return comments

def get_posts_data(driver, publishments_obj, PUBLISHMENT_LINK_CLASS, DESCRIPTION_CLASS, LIKES_CLASS, VIEWS_CLASS, PEOPLE_LIKED_CLASS, COMMENTS_CLASS, COMMENT_CLASS):
    num_posts = 0
    posts = []
    for p in publishments_obj:
        publish = p.find_element(By.CSS_SELECTOR, PUBLISHMENT_LINK_CLASS)
        publish_link = publish.get_attribute("href")
        num_posts += 1
        print(f"Data collected from post: {publish_link}")
        print(f"Number of data posts collected: {num_posts}")
        publish.click()
        time.sleep(1)

        description = get_post_description(driver, DESCRIPTION_CLASS)
        likes = get_post_likes(driver, LIKES_CLASS, VIEWS_CLASS, PEOPLE_LIKED_CLASS)
        comments = get_post_comments(driver, COMMENTS_CLASS, COMMENT_CLASS)

        body = {
            "link": publish_link,
            "description": description,
            "likes": likes,
            "comments": comments
        }
        posts.append(body)

        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.ESCAPE)
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

def save_posts_data(TARGET_USERNAME, posts):
    print("Saving json file...")
    with open(f"{TARGET_USERNAME}.json", "w") as f:
        json.dump({"username": TARGET_USERNAME, "publishments": posts}, f)
    print("Saved.")

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
        self.VIEWS_CLASS = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw" + \
                        ".x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty" + \
                        ".x1943h6x.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
        self.LIKED_BY_CLASS = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw" + \
                            ".x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty" + \
                            ".x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
        
        self.PEOPLE_LIKED_CLASS = ".x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20" + \
                                ".xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619" + \
                                ".x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r" + \
                                ".x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8" + \
                                ".x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz" + \
                                ".xh8yej3.x193iq5w.x1lliihq.x1dm5mii.x16mil14.xiojian.x1yutycm"
        self.OTHER_PEOPLE_CLASS = ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk" + \
                                ".xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5" + \
                                ".x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd"
        
        self.DESCRIPTION_CLASS = "._a9zs"
        self.COMMENTS_CLASS = "._a9ym"
        self.COMMENT_CLASS = "._aacl._aaco._aacu._aacx._aad7._aade"

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

    def init_chromedriver(self, headless=True):
        if headless == True:
            print("Initializing Chrome driver...")
            try:
                op = webdriver.ChromeOptions()
                op.add_argument("headless") # don't open a Chrome window
                self.driver = webdriver.Chrome(executable_path=self.CHROMEDRIVER_PATH, options=op)
                print("Chrome driver initialized.\n")
            except:
                print("Error initializing Chrome driver...\n")
                print_error()
        
        elif headless == False:
            print("Initializing Chrome driver...")
            try:
                # op = webdriver.ChromeOptions()
                # op.add_argument("headless") # don't open a Chrome window
                self.driver = webdriver.Chrome(executable_path=self.CHROMEDRIVER_PATH)#, options=op)
                print("Chrome driver initialized.\n")
            except:
                print("Error initializing Chrome driver...\n")
                print_error()

    def login(self):
        print("Entering the account...")
        try:
            self.driver.get("https://www.instagram.com/")
            time.sleep(3)
            login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            login.send_keys(self.INSTA_USERNAME) # fill username
            passw = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            passw.send_keys(self.INSTA_PASSWORD) # fill password
            time.sleep(0.5)
            passw.send_keys(Keys.ENTER) # press Enter
            time.sleep(10)
            print("Login successfull.\n")
        except:
            print("Login failed...\n")
            print_error()

    def go_to_link(self, l):
        self.driver.get(l)

    def get_posts_link(self):
        self.driver.get(f"https://www.instagram.com/{self.TARGET_USERNAME}")
        time.sleep(3)
        links = []
        publishments_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PUBLISHMENT_CLASS)
        for p in publishments_obj:
            links.append(p.find_element(By.CSS_SELECTOR, self.PUBLISHMENT_LINK_CLASS).get_attribute("href"))
        self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        time.sleep(2)

        count = 0
        while count < 15:
            new_publishments_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PUBLISHMENT_CLASS)
            for p in new_publishments_obj:
                if p not in publishments_obj:
                    links.append(p.find_element(By.CSS_SELECTOR, self.PUBLISHMENT_LINK_CLASS).get_attribute("href"))
            self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            time.sleep(2)

            if publishments_obj == new_publishments_obj:
                count += 1

            publishments_obj = new_publishments_obj
        return links
    
    def get_post_description(self):
        try:
            description = self.driver.find_element(By.CSS_SELECTOR, self.DESCRIPTION_CLASS).find_element(By.TAG_NAME, "h1").text
        except NoSuchElementException:
            description = ""
        return description
    
    def get_post_comments(self):
        try:
            comments_obj = self.driver.find_elements(By.CSS_SELECTOR, self.COMMENTS_CLASS)
            comments = []
            for c in comments_obj:
                comments.append(c.find_element(By.CSS_SELECTOR, self.COMMENT_CLASS).text)
        except NoSuchElementException:
            comments = []
        return comments
    
    def get_post_likes(self):
        try:
            t = self.driver.find_element(By.CSS_SELECTOR, self.LIKES_CLASS).text
            if re.search("like", t) or re.search("curti", t):
                likes = t
            else:
                liked_by_link = [i.get_attribute("href") for i in self.driver.find_elements(By.CSS_SELECTOR, self.OTHER_PEOPLE_CLASS) if re.search("liked_by", i.get_attribute("href"))][0]
                self.driver.get(liked_by_link)
                time.sleep(3)
                people = []
                people_liked_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PEOPLE_LIKED_CLASS)
                for p in people_liked_obj:
                    people.append(p)
                self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
                time.sleep(2)

                count = 0
                while count < 10:
                    new_people_liked_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PEOPLE_LIKED_CLASS)
                    for p in new_people_liked_obj:
                        if p not in people_liked_obj:
                            people.append(p)
                    self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
                    time.sleep(2)

                    if people_liked_obj == new_people_liked_obj:
                        count += 1
                    
                    people_liked_obj = new_people_liked_obj
                
                likes = f"{len(people)} curtidas"

        except NoSuchElementException:
            self.driver.find_elements(By.CSS_SELECTOR, self.VIEWS_CLASS)[-1].click()
            time.sleep(1)
            likes = self.driver.find_element(By.CSS_SELECTOR, "._aauu").text
            print(f"Views Likes - {likes}")
            
        except:
            print("Error getting likes / Views / Liked By.")
            print_error()
            
        return likes