import pickle


## Pickling allows you to store chunks of data as binary
# we can store small amounts of info

############################
# heresandobject = ("field1","field2","field3")


# # make sure WB for write binary
# with open("PICKLERICCKKKK",'wb') as file:
#     pickle.dump(heresandobject,file)

##########################
with open("PICKLERICCKKKK","rb") as file:
    print(file)
    ## if there are multiple items stored in a tuple
    # e.g. (Name1, Name 2)
    # they will return in the same order
    # revivedName1, revivedName2 = pickle.load(names)
    print(pickle.load(file))

