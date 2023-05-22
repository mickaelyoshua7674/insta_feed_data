from instaBot import InstaBot

SECRET_INSTA = "mickaelyoshua_insta"
TARGET_USERNAME = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

bot = InstaBot(TARGET_USERNAME, CHROMEDRIVER_PATH, SECRET_INSTA)

bot.get_publishments_data()

# Last publishment: https://www.instagram.com/p/Uhz86ms_sG/