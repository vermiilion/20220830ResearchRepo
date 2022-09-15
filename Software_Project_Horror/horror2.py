import json

with open('Software_Project_Horror/horror.json') as f:
    data = json.load(f)
    # print(data["name"])
for movie in data["horror_movies"]:
    print(movie["name"],movie["year"])