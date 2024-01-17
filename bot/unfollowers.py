from instaBot import InstaBot
import time, json, os

if not os.path.exists("data/"):
    os.mkdir("data")

# INITIALIZING INSTABOT
with open("secrets.txt", "r") as f:
    login, password = f.read().split(",")
start = time.time()
bot = InstaBot()
bot.login(login, password)

bot.go_to_link("https://www.instagram.com/mickaelyoshua/followers/")
new_followers = bot.get_follow()
bot.go_to_link("https://www.instagram.com/mickaelyoshua/following/")
new_following = bot.get_follow()

with open("data/followers.json", "r") as f:
    loaded_followers = json.load(f)
with open("data/unfollowers.json", "w") as f:
    json.dump(["https://www.instagram.com/"+f for f in new_followers if f not in loaded_followers], f)

with open("data/followers.json", "w") as f:
    json.dump(new_followers, f)
with open("data/following.json", "w") as f:
    json.dump(new_following, f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")