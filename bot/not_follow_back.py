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
followers = bot.get_follow()
with open("data/followers.json", "w") as f:
    json.dump(followers, f)

bot.go_to_link("https://www.instagram.com/mickaelyoshua/following/")
following = bot.get_follow()
with open("data/following.json", "w") as f:
    json.dump(following, f)

with open("data/not_follow_back.json", "w") as f:
    json.dump(["https://www.instagram.com/"+f for f in following if f not in followers], f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")