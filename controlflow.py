#control flow
if 1==1:
    #need a colon to move ino condition result
    #indentation one tab]
    print("IYA")
elif 2 == 2:
    print("else if uses elif in python")
else:
    print("final")

#Lamda expression
print("I'm a lambda") if 1==1 else print("inline if else")

# while loops to break infinite ctrl C

index =1 
while index <  6:
    
    print(f"loop number {index}")
    index += 1
    if index == 4:
        #break statement
        break


## input string on the inside is instructions
## text will remain inline if console.
information = input("please insert something:  ")
## will return string use cast eg int() if looking for numbers
print(information)


## for loops for x in y do x

array = "i'm a string and i'm needed for looping".split()

for item in array:
    print(item)
# if looping over tuples you can "unpack" by formatting as tuple
# parens are optional
list_of_tups = [(1,2),(2,3),(3,4),(5,6)]
for (item1,item2) in list_of_tups:
    print(item1)
    print(item2)

## loops over dictionarys 
## unordered
diction = {"one":"111","two":"222","four":"444","three":"333"}

# keys
for item in diction:
    print(item)

#values 
for itema in diction.items():
    print(itema)

for value,key in diction.items():
    print(value + " " + key)
    
    
for k in diction:
    print(diction[k])
## continue keyword skips logic an returns to loop incrementer
for letter in 'code':
    if letter == 'd':
        continue
    print(letter)