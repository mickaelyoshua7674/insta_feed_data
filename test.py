from instaBot import InstaBot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SECRET_INSTA = "mickaelyoshua_insta"
TATGET_USERNAME = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"


bot = InstaBot(TATGET_USERNAME, CHROMEDRIVER_PATH, SECRET_INSTA)
print(bot.num_publishments)

bot.scroll_down()