from instaBot import InstaBot

USERNAME = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

bot = InstaBot(USERNAME, CHROMEDRIVER_PATH)
print(bot.num_publishments)