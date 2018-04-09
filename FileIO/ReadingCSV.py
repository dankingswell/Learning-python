from csv import reader
## two mode Reader and DictReader
# Reader:

DataInFile = []
with open("blog_data") as file:
    csv_reader = reader(file)
    #moves us foward past headers
    next(csv_reader)
    DataInFile.extend([x[0] for x in csv_reader])

#print(DataInFile)


## Dict reader returns and ordered dictionary of objects
# each row is separated into a list which can be accesed by
# using a key like a regular dictionary dict["name"]
from csv import DictReader
with open("blog_data") as file:
    csv_Reader = DictReader(file)
    #moves us foward past headers
    print(csv_Reader)
    for row in csv_Reader:
        print(row["title"])


## Reader function for both can receive a custom delimiter
# delimeter can be passed as a kw param

with open("blog_data") as file:
    csv_Reader = DictReader(file, delimeter="|")