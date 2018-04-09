# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup as bs
from csv import writer
from time import time,sleep

res = requests.get("https://www.rithmschool.com/blog")
soup = bs(res.text,"html.parser")
articles = soup.select("article")

time_title = ( (x.find("time")["datetime"],x.find("p").get_text()) for x in articles )

# with open("blog_data","w") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["title","date"])
#     for x,y in time_title:
#         csv_writer.writerow([x , y])


def timer(f):
    def wrapper(*args,**kwargs):
        start = time()
        f(*args,**kwargs)
        end = time() - start
        print(end)
    return wrapper

@timer
def requesteee(timer=0):
    sleep(timer)
    res = requests.get("https://www.rithmschool.com/blog")
    soup = bs(res.text,"html.parser")
    articles = soup.select("article")
    print("complete")
    


requesteee()
requesteee(1)
requesteee(3)
