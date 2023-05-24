from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SECRET_INSTA = "mickaelyoshua_insta"
USERNAME_TCEPB = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

VIEWS_CLASS = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw" + \
            ".x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty" + \
            ".x1943h6x.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
LIKED_BY_CLASS = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw" + \
                ".x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty" + \
                ".x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
OTHER_PEOPLE_CLASS = ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk" + \
                    ".xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5" + \
                    ".x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd"

# op = webdriver.ChromeOptions()
# op.add_argument("headless") # don't open a Chrome window
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)#, options=op)
print("Chrome driver initialized.\n")

print("   Entering the account...")

driver.get("https://www.instagram.com/")
time.sleep(4)
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
login.send_keys("mickaelyoshua") # fill username
passw = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
passw.send_keys("***") # fill password
time.sleep(0.5)
passw.send_keys(Keys.ENTER) # press Enter
time.sleep(10)
print("    Login successfull.\n")

driver.get("https://www.instagram.com/p/CsOnaAMr5Mu/")
time.sleep(5)
driver.find_element(By.LINK_TEXT, "outras pessoas").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
time.sleep(10)
driver.quit()