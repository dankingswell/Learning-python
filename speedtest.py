from time import time

def speed_test(func):
    def wrapper(*args,**kwargs):
        begin = time()
        func(*args,**kwargs)
        final = time() - begin
        print(f"total time {final}")
    return wrapper

def myGen(end):
    curr = 1
    while curr <= end:
        yield curr
        curr += 1

@speed_test
def sumNumsGen():
    return sum((x for x in range(10000000)))
sumNumsGen()

@speed_test
def sumNumsList():
    return sum([x for x in range(10000000)])
sumNumsList()

@speed_test
def sumNumsGenSeparate():
    return sum(myGen(10000000))

sumNumsGenSeparate()




