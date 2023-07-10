from instaBot import InstaBot
import json
import time
import os
import random

CHROMEDRIVER_PATH = "chromedriver.exe"
USERNAME = "prefjoaopessoa"

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
with open("secrets.txt", "r") as f:
    login, password = f.read().split(",")
start = time.time()
bot = InstaBot(USERNAME, CHROMEDRIVER_PATH)
bot.init_chromedriver(headless=True)
bot.login(login, password)

# GET POSTS DATA
for l in links:
    if l not in collected_links: # if it wasn't collected
        print(f"Collecting data from {l} ...")
        bot.go_to_link(l)
        time.sleep(random.uniform(5,31))
        if bot.check_page_post_loaded():
            description = bot.get_post_description()
            date = bot.get_post_date()
            comments = bot.get_post_comments()
            likes = bot.get_post_likes()
        else:
            print("\nTime for reload page - 5min...\n")
            time.sleep(5*60)
            bot.go_to_link(l)
            time.sleep(5)
            description = bot.get_post_description()
            date = bot.get_post_date()
            comments = bot.get_post_comments()
            likes = bot.get_post_likes()

        body = {
            "link": l,
            "description": description,
            "comments": comments,
            "likes": likes,
            "date": date
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