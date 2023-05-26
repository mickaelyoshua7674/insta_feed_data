from instaBot import InstaBot
import json
import time

SECRET_INSTA = "mickaelyoshua_insta"
CHROMEDRIVER_PATH = "chromedriver.exe"

USERNAME_TCEPB = "tcepb"

start = time.time()
bot_tcepb = InstaBot(USERNAME_TCEPB, CHROMEDRIVER_PATH, SECRET_INSTA)
bot_tcepb.init_chromedriver(headless=True)
bot_tcepb.login()
links = bot_tcepb.get_posts_link()
bot_tcepb.driver_quit()

with open(f"{USERNAME_TCEPB}_posts_link.json", "w") as f:
    json.dump(links, f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")


USERNAME_PREF_JAMPA = "prefjoaopessoa"

start = time.time()
bot_pref_jampa = InstaBot(USERNAME_PREF_JAMPA, CHROMEDRIVER_PATH, SECRET_INSTA)
bot_pref_jampa.init_chromedriver(headless=True)
bot_pref_jampa.login()
links = bot_pref_jampa.get_posts_link()
bot_pref_jampa.driver_quit()

with open(f"{USERNAME_PREF_JAMPA}_posts_link.json", "w") as f:
    json.dump(links, f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")