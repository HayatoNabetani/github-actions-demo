import requests
res = requests.get("https://yahoo.com")
print(res.text[0:10])