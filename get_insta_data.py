from instaBot import InstaBot

SECRET_INSTA = "mickaelyoshua_insta"
USERNAME_TCEPB = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

bot_tcepb = InstaBot(USERNAME_TCEPB, CHROMEDRIVER_PATH, SECRET_INSTA)
bot_tcepb.get_publishments_data()

# Last publishment: https://www.instagram.com/p/Uhz86ms_sG/