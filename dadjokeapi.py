import requests 
from random import randint

def JokeMaker():

    while True:
        if input("would you like to hear a joke? (Y/N)") != "Y":
            break

        jokeReq = input("What kind of joke would you like to hear?: \t")


        r = requests.get("https://icanhazdadjoke.com/search",headers = {
            "Accept" : "application/json"
        }, params = {
            "term" : jokeReq
        }
        ).json()
        listOfJokes = r["results"]
        searchIndex = None if len(listOfJokes)  == 0 else randint(0,r["total_jokes"]-1)
        sToPrint = f"sorry i don't know any about {jokeReq}" if not len(listOfJokes) > 0 else f"here's one:\n {listOfJokes[searchIndex]['joke']}" 
        print(sToPrint)
        

JokeMaker()