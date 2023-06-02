import requests

response = requests.get("https://www.instagram.com/p/CMerJgap0dr/")
print(response.status_code)
print(response.text)