from instaBot import InstaBot
import time, json

CHROMEDRIVER_PATH = "/usr/lib/chromium-browser/chromedriver"
USERNAME = "mickaelyoshua"

# INITIALIZING INSTABOT
with open("secrets.txt", "r") as f:
    login, password = f.read().split(",")
start = time.time()
bot = InstaBot(USERNAME, CHROMEDRIVER_PATH)
bot.init_chromedriver(headless=True)
bot.login(login, password)

bot.go_to_link(f"https://www.instagram.com/{USERNAME}/followers/")
new_followers = bot.get_follow()
bot.go_to_link(f"https://www.instagram.com/{USERNAME}/following/")
new_following = bot.get_follow()

with open("data_mickaelyoshua/followers.json", "r") as f:
    loaded_followers = json.load(f)
with open("data_mickaelyoshua/unfollowers.json", "w") as f:
    json.dump(["https://www.instagram.com/"+f for f in new_followers if f not in loaded_followers], f)

with open("data_mickaelyoshua/followers.json", "w") as f:
    json.dump(new_followers, f)
with open("data_mickaelyoshua/following.json", "w") as f:
    json.dump(new_following, f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")