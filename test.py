from instaBot import InstaBot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SECRET_INSTA = "mickaelyoshua_insta"
TARGET_USERNAME = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

bot = InstaBot(TARGET_USERNAME, CHROMEDRIVER_PATH, SECRET_INSTA)
print(bot.num_publishments)

bot.scroll_down()



# Last publishment loaded: https://www.instagram.com/p/yfMELws_q2/