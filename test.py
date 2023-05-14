from instaBot import InstaBot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"
IMAGE_CLASS = ".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3"
BUTTON_LOGIN_X_CLASS = "._abn5._abn6._aa5h"
BUTTON_LOAD_MORE_CLASS = "._a9-r._a9-s._a9-u.x6s0dn4.x1iorvi4.xn6708d.xs9asl8.x1ye3gou.x10l6tqk.xsms3ob.xkrlcpk.xubyhnz"


bot = InstaBot(USERNAME, CHROMEDRIVER_PATH)
print(bot.num_publishments)

try:
    # op = webdriver.ChromeOptions()
    # op.add_argument("headless") # don't open a Chrome window
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)#, options=op)
    print("Chrome driver initialized.\n")
except:
    print("Error initializing Chrome driver...\n")

driver.get(f"https://www.instagram.com/{USERNAME}/")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, BUTTON_LOGIN_X_CLASS).click()
time.sleep(1)

publishments = driver.find_elements(By.CSS_SELECTOR, IMAGE_CLASS)
qtd_publishments = len(publishments)

driver.execute_script("arguments[0].scrollIntoView(true);", publishments[-1]) # scroll down to last follower showing on list
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, BUTTON_LOAD_MORE_CLASS).click()
time.sleep(1)

while qtd_publishments < bot.num_publishments:
    publishments = driver.find_elements(By.CSS_SELECTOR, IMAGE_CLASS)
    qtd_publishments = len(publishments)
    driver.execute_script("arguments[0].scrollIntoView(true);", publishments[-1])

driver.quit()




# while True:
#     new_follower_obj = driver.find_elements(By.CSS_SELECTOR, self.css_selector_followers) # get new list of followers
#     if len(new_follower_obj) >= self.num_followers-3: # when all followers are loaded on page exit the loop
#         break
#     else:
#         driver.execute_script("arguments[0].scrollIntoView(true);", new_follower_obj[-1]) # scroll down to last follower showing on list
#         follower_obj = new_follower_obj # update previous followers to get the new followers