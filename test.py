from instaBot import InstaBot
import time
import json

SECRET_INSTA = "mickaelyoshua_insta"
CHROMEDRIVER_PATH = "chromedriver.exe"
USERNAME = "neymarjr"

bot = InstaBot(USERNAME, CHROMEDRIVER_PATH, SECRET_INSTA)
bot.init_chromedriver(headless=False)
bot.login()

l = "https://www.instagram.com/p/Ctwnq2XL1qa/"

print(f"Collecting data from {l} ...")
bot.go_to_link(l)
time.sleep(5)
if bot.check_page_post_loaded():
    date = bot.get_post_date()
else:
    print("\nTime for reload page - 5min...\n")
    time.sleep(5*60)
    bot.go_to_link(l)
    time.sleep(5)
    date = bot.get_post_date()

with open("test.json", "w") as f:
    json.dump(date, f)