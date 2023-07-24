from instaBot import InstaBot
import time, json

CHROMEDRIVER_PATH = "chromedriver.exe"
USERNAME = "mickaelyoshua"

# INITIALIZING INSTABOT
with open("secrets.txt", "r") as f:
    login, password = f.read().split(",")
start = time.time()
bot = InstaBot(USERNAME, CHROMEDRIVER_PATH)
bot.init_chromedriver(headless=False)
bot.login(login, password)

bot.go_to_link(f"https://www.instagram.com/{USERNAME}/followers/")
followers = bot.get_follow()
with open("followers.json", "w") as f:
    json.dump(followers, f)

bot.go_to_link(f"https://www.instagram.com/{USERNAME}/following/")
following = bot.get_follow()
with open("following.json", "w") as f:
    json.dump(following, f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")