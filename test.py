from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SECRET_INSTA = "mickaelyoshua_insta"
USERNAME_TCEPB = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

PEOPLE_LIKED_CLASS = ".x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20" + \
                    ".xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619" + \
                    ".x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r" + \
                    ".x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8" + \
                    ".x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz" + \
                    ".xh8yej3.x193iq5w.x1lliihq.x1dm5mii.x16mil14.xiojian.x1yutycm"

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
passw.send_keys("******") # fill password
time.sleep(0.5)
passw.send_keys(Keys.ENTER) # press Enter
time.sleep(10)
print("    Login successfull.\n")


driver.get("https://www.instagram.com/p/CsOnaAMr5Mu/")
time.sleep(5)
c = 0
driver.find_element(By.LINK_TEXT, "outras pessoas").click()
time.sleep(5)
last = driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS)[-1]
driver.execute_script("arguments[0].scrollIntoView(true);", last)

while c < 30:
    time.sleep(1)
    new_last = driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS)[-1]
    driver.execute_script("arguments[0].scrollIntoView(true);", last)
    if last == new_last:
        c += 1
    last = new_last
likes = len(driver.find_elements(By.CSS_SELECTOR, PEOPLE_LIKED_CLASS))
print(likes)
time.sleep(10)
driver.quit()