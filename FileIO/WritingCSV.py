from csv import writer,reader


# open in write mode
with open("aNewCSV","w") as file:
    # give writer stream access to file
    Write = writer(file)
    Write.writerow(["Name","text","Fruit"])
    Write.writerow(["Gimly","i have an axe","no thankyou"])
