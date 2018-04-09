##print("Hello World")

def iya (hellophrase):
    ##print(hellophrase)

iya("IYAAAAA")

my_list = [1,2,3]


#lists are passed by reference.
x = my_list.reverse()
##print(my_list)
my_list.insert(1,10)
##print(my_list)
my_list.extend(['hello','extension'])
##print(my_list)
my_list.insert(0,["cece","cecec"])
##print(my_list)

# dictionarys
my_dictionary = {"string":"Ola", "int":0,
"double":1.1}

#new key
my_dictionary["NewKey"] = "Hi i'm new"
my_dictionary["Array"] = ["Hello","Darkness","my old","friend"]

##print(my_dictionary["NewKey"])

#Tuples immuteable, no index in list syntax, can refer to items by values
tups =(1,2,3)

##print(tups.index(2))
#tuple values cannot be re assigned

#Sets no index, unique elements only wil convert [1,2,1] to {1,2}
x = set()
x.add(1)
# x will == 1
##print (x)

unique_set = set([1,2,1])
# set will == 1,2
for item in unique_set:
    ##print (item)

#Bools true and false as usual capital T and F
# None place holder== None can be used to add unassigned data.unique_set

c = None

