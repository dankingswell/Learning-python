from csv import DictReader,DictWriter

Data = []

with open("blog_data") as file:
    Read =  DictReader(file)
    for x in Read:
        Data.append(x)

        
with open("blog_dataReWrite","w") as file:
    Header = ["Date","Title"]
    Writer = DictWriter(file,fieldnames=Header)
    Writer.writeheader()
    for x in Data:
        Writer.writerow({ 
            "Title":x["title"][:45]+"...",
            "Date":x["date"]
         })


