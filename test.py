from instaBot import *

SECRET_INSTA = "mickaelyoshua_insta"
TARGET_USERNAME = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

PUBLISHMENT_CLASS = "._aabd._aa8k._al3l"
PUBLISHMENT_LINK_CLASS = ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk" + \
                        ".xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5" + \
                        ".x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd"
IMAGE_CLASS = ".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3"

LIKES_CLASS = ".x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
VIEWS_CLASS = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw" + \
                ".x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty" + \
                ".x1943h6x.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
LIKED_BY_CLASS = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw" + \
                    ".x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty" + \
                    ".x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"

PEOPLE_LIKED_CLASS = ".x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20" + \
                    ".xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619" + \
                    ".x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r" + \
                    ".x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8" + \
                    ".x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz" + \
                    ".xh8yej3.x193iq5w.x1lliihq.x1dm5mii.x16mil14.xiojian.x1yutycm"
OTHER_PEOPLE_CLASS = ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk" + \
                    ".xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5" + \
                    ".x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd"

DESCRIPTION_CLASS = "._a9zs"
COMMENTS_CLASS = "._a9ym"
COMMENT_CLASS = "._aacl._aaco._aacu._aacx._aad7._aade"

def print_error():
    """Print the error message and exit script."""
    traceback.print_exc()
    print("Closing...")
    sys.exit()

driver = init_chromedriver(CHROMEDRIVER_PATH, headless=False)

login(driver, "mickaelyoshua", "*****")

time.sleep(3)

links = ["https://www.instagram.com/p/Cr1aiWnpSSG/", "https://www.instagram.com/p/Cr3p3-trE0o/", "https://www.instagram.com/p/CsCNwOFppsb/", "https://www.instagram.com/p/CsOnaAMr5Mu/"]

likes = []
for l in links:
    driver.get(l)
    time.sleep(3)
    t = driver.find_element(By.CSS_SELECTOR, LIKES_CLASS).text
    print(f"t - {t}")
    if re.search("like", t) or re.search("curti", t):
        likes = t
        print(f"Likes - {likes}")
    else:
        try:
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
            print(f"People likes - {likes}")
            # liked.append(driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS))
            # last = liked[-1]
            #driver.execute_script("arguments[0].scrollIntoView(true);", last)

        #     while c < 15:
        #         time.sleep(1)
        #         for f in driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS):
        #             if f not in liked:
        #                 liked.append(f)

        #         new_last = liked[-1]
        #         driver.execute_script("arguments[0].scrollIntoView(true);", last)
                
        #         if last == new_last:
        #             c += 1
        #         last = new_last
        #     likes = f"{len(driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS))} likes"
        #     print(f"People Likes - {likes}")
        #     driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.ESCAPE)
        # except NoSuchElementException:
        #     try:
        #         driver.find_elements(By.CSS_SELECTOR, VIEWS_CLASS)[-1].click()
        #         time.sleep(1)
        #         likes = driver.find_element(By.CSS_SELECTOR, "._aauu").text
        #         print(f"Views Likes - {likes}")
        #     except NoSuchElementException:
        #         pass
        except:
            print("Error getting likes / Views / Liked By.")
            print_error()

# print(len(likes))
# print(likes)