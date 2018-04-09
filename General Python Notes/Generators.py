# uses yield not return
# generator is an iterator 

def count_to (max):
    count = 1
    while count <= max:
        yield count
        count += 1
        
# yield returns value then awaits next before continuing
counter  = count_to(5)

print(counter)
# will not work on it's own as is just stored forumla
print(next(counter))
# next calls the current "state" of the generator
# yield knows it's now holding one but not 0
# because of this it will increment by one

print(next(counter))
# help(counter) for methods on object
# a for loop on this object for from this point will start at 2 and move onto three
for x in counter:
    print(x)
## when the iterator hit's the maximum the error will be handled by the __iter__ method and will stop the generator

## generator expression
inline = ( num for num in range (10))
## doesn't require use of yield keyword but will use it when returning data
for x in inline :
    print (x) 