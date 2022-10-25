import json
data = json.load(open('applied\Data\data.json', 'r'))
print(type(data))
count = 0
for i in data["item"].keys():
    if "stats" in data["item"][i].keys():
        
        if data["item"][i]["stats"]["bonus"]: #checks if dict is empty if not print the bonuses
            print(data["item"][i]["stats"]["bonus"])
            count +=1
        #print(data["item"][i]["name"]+': ',data["item"][i]["stats"])
print(count)
#print(data["item"]["12439"]["name"])