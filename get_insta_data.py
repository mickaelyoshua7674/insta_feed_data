from instaBot import InstaBot
import time

SECRET_INSTA = "mickaelyoshua_insta"
USERNAME_TCEPB = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

start = time.time()
bot_tcepb = InstaBot(USERNAME_TCEPB, CHROMEDRIVER_PATH, SECRET_INSTA)
bot_tcepb.init_chromedriver(headless=False)
bot_tcepb.login()
links = bot_tcepb.get_posts_link()

print(len(links))
print(links)