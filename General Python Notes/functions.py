## returns value
def addthem(a,b):
    return a + b
value = addthem(1,2)
print(value)

## if no return saving to values will not work
def noreturn(num):
    num + 1
    print("no return")

a = noreturn(1)

## optional params