import requests
res = requests.get("https://yahoo.com")
str2 = res.text[0:10]

with open("log.txt", "w") as f:
    f.write(str2)
