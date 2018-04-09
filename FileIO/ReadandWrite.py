from csv import reader,writer

with open("blog_data") as file:
    Reader = reader(file)

    Changed = [ [f"{x[1][:45]}...", x[0]] for x in Reader]
    for x in Changed:
        print(x)

with open("TransmitData","w") as file:
    Writer = writer(file)
    for x in Changed:
        Writer.writerow(x)


## concise version


with open("blog_data") as file:
    Reader = reader(file)
    with open("TransmitData2","w") as file:
        Writer = writer(file)
        for x in [ [f"{x[1][:45]}...", x[0]] for x in Reader]:
            Writer.writerow(x)