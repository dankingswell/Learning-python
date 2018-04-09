## list comprehension is an inline forloop

## take all chars in string and place in array
MyList = []
s = "thisismystring"
## place inside of brackets as making a list
# a with any changes for each a in b
newlists = [letter for letter in s]
print(newlists)


## do something to a for each a in b
square = [x**2 for x in range(1,11)]
print(square)

## if statements at the end of info
evens = [item for item in range(1,11) if  item % 2 == 0 ]
print(evens)

## if as terenary means lambda first
finallist = [x  if  x % 2 == 0 else "nope" for x in range(1,11)]
print(finallist)