import json

with open("tcepb.json", "r") as f:
    data = json.load(f)

print(data["publishments"][0]["description"])