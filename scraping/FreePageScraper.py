import requests
from csv import DictWriter
from bs4 import BeautifulSoup as bs
from time import sleep


SeedURL = "https://en.wikipedia.org/wiki/Web_scraping"
def scrapeResponse(url):
    try:
        return requests.get(url)
    except:
        return False

def FirstLinkFinder(soup):
    link = soup.select("p a[href]")[0]["href"]
    splitLink = link.split("/")
    splitSeed = SeedURL.split("/")
    try:
        splitSeed[-1],splitSeed[-2] = splitLink[2],splitLink[1]
    except:
        return False
    return "/".join(splitSeed)


Data = []

## loop while pages < 10

index = 0 
while index < 5:
    index += 1
    # start from seed page
    res =  scrapeResponse(SeedURL)
    if not res:
        break
    soup = bs(res.text,"html.parser")
    # take title of page
    Title =  soup.find("h1").get_text()
    # go through page take all headers
    HeadLines = [x.get_text() for x in soup.select(".mw-headline")]
    # go to next url "first A tag in content"
    SeedURL = FirstLinkFinder(soup)
    if not SeedURL:
        break
    print(SeedURL)
    # add all data ready for exporting
    Data.append({
        "title":Title,
        "headlines" : HeadLines,
        "seed" : SeedURL
        })
    # wait a 2 seconds
    sleep(2)

#Send data to CSV
with open("WikiScrapingCSV",'w') as file:
    Headers = ["title","headlines","seed"]
    Writer = DictWriter(file,fieldnames=Headers)
    Writer.writeheader()
    for x in Data:
        Writer.writerow({
            "title" : x["title"],
            "headlines" : x["headlines"],
            "seed": x["seed"]

        })
#end