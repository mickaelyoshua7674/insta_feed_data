from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, re, random
from typing import List

class InstaBot:
    def __init__(self) -> None:
        self.TARGET_USERNAME = "mickaelyoshua"
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
        
        self.POST_BODY_CLASS = ".x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3"

        self.COMMENTS_BOX = ".x9f619.x5yr21d.x10l6tqk.xh8yej3.xexx8yu.x4uap5.x18d9i69.xkhd6sd"
        self.MORE_COMMENTS_CLASS = ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xdj266r" + \
                                ".xat24cr.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf" + \
                                ".xqjyukv.x1qjc9v5.x1oa3qoh.xl56j7k"

        self.DESCRIPTION_CLASS = "._a9zs"
        self.COMMENTS_CLASS = "._a9ym"
        self.COMMENT_CLASS = "._aacl._aaco._aacu._aacx._aad7._aade"

        self.DATE_CLASS = "._aacl._aaco._aacu._aacx._aad6._aade._aaqb"

        self.FOLLOWBOX_CLASS_1 = ".x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe"
        self.FOLLOWBOX_CLASS_2 = ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek" + \
                                ".xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1"
        self.FOLLOW_CLASS = ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"
        self.FOLLOWER_CLASS = ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6" + \
                            ".x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1"
        
        print("Initializing Chrome driver...")
        op = webdriver.ChromeOptions()
        op.add_argument("headless") # don't open a Chrome window
        self.driver = webdriver.Remote("http://chrome:4444", options=op)
        print("Chrome driver initialized.\n")

    def get_follow(self) -> List[str]:
        """Get a list of all follow"""
        print("Getting list...\nCount:")
        follow = set()
        objs = self.driver.find_element(By.CSS_SELECTOR, self.FOLLOWBOX_CLASS_1)\
            .find_element(By.CSS_SELECTOR, self.FOLLOWBOX_CLASS_2)\
            .find_elements(By.CSS_SELECTOR, self.FOLLOW_CLASS)
        self.random_sleep(1,3)
        for f in objs:
            follow.add(f.find_element(By.CSS_SELECTOR, self.FOLLOWER_CLASS).text)
        last_len = len(follow)
        count = 0
        while count < 12:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", objs[-1])
            self.random_sleep(2,4)
            objs = self.driver.find_element(By.CSS_SELECTOR, self.FOLLOWBOX_CLASS_1)\
                .find_element(By.CSS_SELECTOR, self.FOLLOWBOX_CLASS_2)\
                .find_elements(By.CSS_SELECTOR, self.FOLLOW_CLASS)
            self.random_sleep(1,3)
            for f in objs:
                follow.add(f.find_element(By.CSS_SELECTOR, self.FOLLOWER_CLASS).text)
            new_len = len(follow)
            if last_len == new_len:
                count += 1
            print(new_len)
            last_len = new_len
        print("Finished.\n")
        return list(follow)

    def random_sleep(self, i: int, f: int) -> None:
        """Randomly choose a float number between i-f and sleep during that random time"""
        time.sleep(random.uniform(i, f))

    def check_page_post_loaded(self) -> bool:
        """If element is found return True"""
        try:
            self.random_sleep(1,3)
            self.driver.find_element(By.CSS_SELECTOR, self.POST_BODY_CLASS)
            self.random_sleep(1,3)
            return True
        except NoSuchElementException:
            return False

    def login(self, login: str, password: str) -> None:
        """Make login into account passed when initialized the object class"""
        print("Entering the account...")
        self.driver.get("https://www.instagram.com/")
        self.random_sleep(5,7)
        login_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.random_sleep(1,3)
        login_field.send_keys(login) # fill username
        self.random_sleep(1,3)
        passw = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.random_sleep(1,3)
        passw.send_keys(password) # fill password
        self.random_sleep(1,3)
        passw.send_keys(Keys.ENTER) # press Enter
        self.random_sleep(5,7)
        print("Login successfull.\n")

    def go_to_link(self, l: str) -> None:
        """Go to given link"""
        self.driver.get(l)
        self.random_sleep(5,7)

    def driver_quit(self) -> None:
        """Quit the driver instance"""
        self.driver.quit()

    def get_posts_link(self) -> List[str]:
        """Collect the link of all posts in profile target"""
        links = []
        publishments_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PUBLISHMENT_CLASS)
        self.random_sleep(1,3)
        for p in publishments_obj:
            links.append(p.find_element(By.CSS_SELECTOR, self.PUBLISHMENT_LINK_CLASS).get_attribute("href"))
        self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        self.random_sleep(2,3)

        count = 0
        while count < 15:
            new_publishments_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PUBLISHMENT_CLASS)
            self.random_sleep(1,3)
            for p in new_publishments_obj:
                if p not in publishments_obj:
                    links.append(p.find_element(By.CSS_SELECTOR, self.PUBLISHMENT_LINK_CLASS).get_attribute("href"))
            self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            self.random_sleep(2,3)

            if publishments_obj == new_publishments_obj:
                count += 1

            publishments_obj = new_publishments_obj
        return links
    
    def get_post_description(self) -> str:
        """Get description from post"""
        try:
            description = self.driver.find_element(By.CSS_SELECTOR, self.DESCRIPTION_CLASS).find_element(By.TAG_NAME, "h1").text
            self.random_sleep(1,3)
        except NoSuchElementException:
            description = ""
        return description

    def check_more_comments(self) -> bool:
        """If element is found return True"""
        try:
            self.random_sleep(1,3)
            self.driver.find_element(By.CSS_SELECTOR, self.COMMENTS_BOX).find_element(By.CSS_SELECTOR, self.MORE_COMMENTS_CLASS)
            self.random_sleep(1,3)
            return True
        except NoSuchElementException:
            return False

    def get_post_comments(self) -> List[str]:
        """load all comments and collect then"""
        while self.check_more_comments():
            self.driver.find_element(By.CSS_SELECTOR, self.COMMENTS_BOX).find_element(By.CSS_SELECTOR, self.MORE_COMMENTS_CLASS).click()
            self.random_sleep(2,3)
        try:
            comments_obj = self.driver.find_elements(By.CSS_SELECTOR, self.COMMENTS_CLASS)
            self.random_sleep(1,3)
            comments = []
            for c in comments_obj:
                comments.append(c.find_element(By.CSS_SELECTOR, self.COMMENT_CLASS).text)
        except NoSuchElementException:
            comments = []
        return comments
    
    def get_post_likes(self) -> int:
        """collect the number of likes in post"""
        try:
            t = self.driver.find_element(By.CSS_SELECTOR, self.LIKES_CLASS).text
            self.random_sleep(1,3)
            if re.search("like", t) or re.search("curti", t):
                likes = t
            else:
                liked_by_link = [i.get_attribute("href") for i in self.driver.find_elements(By.CSS_SELECTOR, self.OTHER_PEOPLE_CLASS) if re.search("liked_by", i.get_attribute("href"))][0]
                self.random_sleep(1,3)
                self.driver.get(liked_by_link)
                self.random_sleep(2,3)
                people = []
                people_liked_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PEOPLE_LIKED_CLASS)
                self.random_sleep(1,3)
                for p in people_liked_obj:
                    people.append(p)
                self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
                self.random_sleep(2,3)

                count = 0
                while count < 10:
                    new_people_liked_obj = self.driver.find_elements(By.CSS_SELECTOR, self.PEOPLE_LIKED_CLASS)
                    self.random_sleep(1,3)
                    for p in new_people_liked_obj:
                        if p not in people_liked_obj:
                            people.append(p)
                    self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
                    self.random_sleep(2,3)

                    if people_liked_obj == new_people_liked_obj:
                        count += 1
                    
                    people_liked_obj = new_people_liked_obj
                
                likes = f"{len(people)} likes"
            return int(re.sub("(\.)|(,)", "", likes.split(" ")[0]))

        except NoSuchElementException:
            self.driver.find_elements(By.CSS_SELECTOR, self.VIEWS_CLASS)[-1].click()
            self.random_sleep(1,3)
            likes = self.driver.find_element(By.CSS_SELECTOR, "._aauu").text
            self.random_sleep(1,3)
            return int(re.sub("(\.)|(,)", "", likes.split(" ")[0]))
    
    def get_post_date(self) -> str:
        """Get publishment date of post (datetime)"""
        date = self.driver.find_element(By.CSS_SELECTOR, self.DATE_CLASS).find_element(By.TAG_NAME, "time").get_attribute("datetime")
        self.random_sleep(1,3)
        return date