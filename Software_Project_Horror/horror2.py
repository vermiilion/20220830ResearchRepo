import json

with open('horror2.json') as f:
    data = json.load(f)
    print(data["year"])
# for movie in data["horror_movies"]:
#     print(movie,["year"])