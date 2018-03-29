##  imports from library import item
# comma to add more items * for all
from random import shuffle,randint
y = [10,20,30,40,50]
# shuffle works by reference does not return
shuffle(y)
print(y)

print(randint(1,2000))

## docstring

def name (para):
    """
    docstring
    """
    print(para)
name("parap")
## range takes index inclusive and end point exclusive
# index, endpoint, steps
for num in range(1,11):
    print(num)

# creates list with range given
newList = list(range(1,11))
print(newList)

# enumerate function
#makes a tuple and returns index and item in tuple

for index,letter in enumerate("abcs"):
    print(f"{index},{letter}")

Enumerated = list(enumerate("jnfwlnde"))
print (Enumerated)

## Zip function joins lists into tuple
# will only go as far as shortest list
first = [1,2,3,4,5]
second = "a b c d e".split()

for item in zip(first,second):
    print(item)

## in operator returns bool looks for a in b
print("x" in ("Hello x"))

##index gives index location
# errors if not found
print("hellox".index("x"))

#min and max
min([1,2,3])
max([1,2,3])

