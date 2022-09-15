# import json


# with open('horror.json') as f:
#    data = json.load(f)


# user_input = input("choose a subcategory: slasher, psychological, body horror, religion, supernatural, sci-fi, mystery, urban legend, found footage, monster, comedy, home invasion: ")


# for movie in data["horror_movies"]:
#    genre = (movie["subcategories"])
#    print(type(genre))


   # print(movie[1],["name"],["year"])

   
# hedwig = [1,2,3,4,5,6,7,8]
# print(hedwig[2])
# alfred = [hedwig]
# print(alfred[0][3])

import random
slasher = ["Scream (1996)", "Candyman (1992)", "Texas Chainsaw Massacre (1974)", "Halloween (1978)", "X (2022)",
           "Psycho (1960)"]
body_horror = ["Saw (2004)", "Titane (2021)", "Cabin Fever (2002)", "The Fly (1986)", "Eraserhead (1978)"]
supernatural = ["The Omen (1976)", "The Conjuring (2013)", "Poltergeist (1982)", "The Exorcist (1973)",
                "Shutter (2004)", "Rosemary's Baby (1968)", "Suspiria (1977)", "IT (1990)", "Ringu (1998)"]
found_footage = ["The Blair Witch Project (1999)", "Creep (2014)", "V/H/S (2012)", "Hell House LLC (2015)",
                 "REC (2007)", "The Taking of Deborah Logan (2017)"]
psychological = ["The Shining (1980)", "Mother! (2017)", "Get Out (2017)", "Rosemary's Baby (1968)", "Psycho (1960)",
                 "The Silence of the Lambs (1991)", "Creep (2014)"]
home_invasion = ["The Strangers (2008)", "Don't Breathe (2016)", "Us (2019)", "You're Next (2011)", "Hush (2016)"]
monster = ["Annihilation (2018)", "IT (1990)", "The Thing (1972)", "Jeepers Creepers (2001)", "A Quiet Place (2018)",
           "A Girl Walks Home Alone at Night (2014)", "Let The Right One In (2008)", "The Fly (1986)"]
horror_movies = [slasher, body_horror, supernatural, found_footage, psychological, home_invasion, monster]

user_input = input("Input a horror subgenre - slasher, body_horror, supernatural, found_footage, psychological,/" 
                   "home_invasion, monster: ")
for user_input in horror_movies:
    if user_input == slasher:
        print("You should watch: ", random.choice(slasher))
    elif user_input == body_horror:
        print("You should watch: ", random.choice(body_horror))
    elif user_input == supernatural:
        print("You should watch: ", random.choice(supernatural))
    elif user_input == found_footage:
        print("You should watch: ", random.choice(found_footage))
    elif user_input == psychological:
        print("You should watch: ", random.choice(psychological))
    elif user_input == home_invasion:
        print("You should watch: ", random.choice(home_invasion))
    elif user_input == monster:
        print("You should watch: ", random.choice(monster))

