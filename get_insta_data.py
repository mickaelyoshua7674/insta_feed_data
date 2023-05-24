from instaBot import InstaBot
import time

SECRET_INSTA = "mickaelyoshua_insta"
USERNAME_TCEPB = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

start = time.time()
bot_tcepb = InstaBot(USERNAME_TCEPB, CHROMEDRIVER_PATH, SECRET_INSTA)
bot_tcepb.get_publishments_data()
print(f"\nTime of execution: {time.time() - start}s / {(time.time() - start)/60}min / {((time.time() - start)/60)/60}hrs")

# Last publishment: https://www.instagram.com/p/Uhz86ms_sG/