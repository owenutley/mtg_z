import json

f = open("mtg-gross-card-list.json", "r")

data = json.load(f)
for i in range(50):
    print(data[i]["name"])

f.close()
