from instaBot import InstaBot
import json
import time

SECRET_INSTA = "mickaelyoshua_insta"
USERNAME_TCEPB = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

start = time.time()
bot_tcepb = InstaBot(USERNAME_TCEPB, CHROMEDRIVER_PATH, SECRET_INSTA)
bot_tcepb.init_chromedriver(headless=True)
bot_tcepb.login()
links = bot_tcepb.get_posts_link()
with open(f"{USERNAME_TCEPB}_posts_link.json", "w") as f:
    json.dump(links, f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")