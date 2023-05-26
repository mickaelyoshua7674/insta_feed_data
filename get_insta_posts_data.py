from instaBot import InstaBot
import json
import time

SECRET_INSTA = "mickaelyoshua_insta"
USERNAME_TCEPB = "tcepb"
CHROMEDRIVER_PATH = "chromedriver.exe"

with open(f"{USERNAME_TCEPB}_posts_link.json", "r") as f:
    links = json.load(f)

start = time.time()
bot_tcepb = InstaBot(USERNAME_TCEPB, CHROMEDRIVER_PATH, SECRET_INSTA)
bot_tcepb.init_chromedriver(headless=True)
bot_tcepb.login()

posts = []
for l in links:
    bot_tcepb.go_to_link(l)
    time.sleep(3)
    description = bot_tcepb.get_post_description()
    comments = bot_tcepb.get_post_comments()
    likes = bot_tcepb.get_post_likes()

    posts.append({
        "link": l,
        "description": description,
        "comments": comments,
        "likes": likes
    })
    print(f"Data collected from {l}")

with open(f"{USERNAME_TCEPB}_posts_data.json", "w") as f:
    json.dump(posts, f)

print(f"Execution time: {time.time()-start}s / {(time.time()-start)/60}min / {((time.time()-start)/60)/60}hrs")