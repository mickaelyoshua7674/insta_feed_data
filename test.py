import json

body = {
        "link": "instagram.com",
        "description": "comemoração",
        "comments": ["eba", "opa"],
        "likes": "36 curtidas"
    }

with open("test.json", "r") as f:
    data = json.load(f)

with open("test.json", "w") as f:
    data.append(body)
    json.dump(data, f)