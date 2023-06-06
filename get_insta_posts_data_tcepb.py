from instaBot import InstaBot
import json
import time
import os

SECRET_INSTA = "mickaelyoshua_insta"
CHROMEDRIVER_PATH = "chromedriver.exe"
USERNAME = "tcepb"

start = time.time()
# GETTING LINKS OF POSTS
print("Getting posts links...")
with open(f"{USERNAME}_posts_link.json", "r") as f:
    links = json.load(f)
print("Posts links collected.\n")

# GET LINKS WITH DATA ALREADY COLLECTED
print("Getting link with data collected...")
if os.path.exists(f"{USERNAME}_posts_data.json"): # if there is data collected
    with open(f"{USERNAME}_posts_data.json", "r") as f:
        data = json.load(f)
    collected_links = [l["link"] for l in data]
    print("Links collected.\n")
else: # if there is no data collected
    with open(f"{USERNAME}_posts_data.json", "w") as f:
        json.dump([], f)
    collected_links = []
    print("There is no data collected.\n")

# INITIALIZING INSTABOT
start = time.time()
bot = InstaBot(USERNAME, CHROMEDRIVER_PATH, SECRET_INSTA)
bot.init_chromedriver(headless=True)
bot.login()

# GET POSTS DATA
for l in links:
    if l not in collected_links: # if it wasn't collected
        print(f"Collecting data from {l} ...")
        bot.go_to_link(l)
        time.sleep(30)
        description = bot.get_post_description()
        comments = bot.get_post_comments()
        likes = bot.get_post_likes()

        body = {
            "link": l,
            "description": description,
            "comments": comments,
            "likes": likes
        }
        print(f"Data collected from {l}")
        print("Saving data...")
        with open(f"{USERNAME}_posts_data.json", "r") as f:
            data = json.load(f)
        with open(f"{USERNAME}_posts_data.json", "w") as f: # append data and save
            data.append(body)
            json.dump(data, f)
        print("Data saved.\n")

bot.driver_quit()

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")