# class keyword and self key word
# init acts as c# constructor
class Agent ():

    def __init__(self,RealName):
        self.RealName = RealName

    code = True

    def catchPhrase(self):
        print("i'm going to be the Codage")

    def coder (self):
        if self.code:
            print("Yes")
        else:
            print("no")

    ## private methods start with _ single underscore
 
    def _privateMethod(self):
        print("Private method")

# vars in class act as fields

dan = Agent("Dan")
print(dan.code)
print(dan.RealName)
dan.catchPhrase()
dan.coder()

## Inheritance

class Person():
    def __init__(self,f,l):
        self.First = f
        self.Last = l

    def reportForDuty(self):
        print(f"i am {self.First} {self.Last}")

    def hello(self):
        print(f"Hello i am {self.First}")

# pass class as param
class SecretAgent(Person):
    def __init__(self,f,l,code):
        #Call init to use Person Constructor
        Person.__init__(self,f,l)
        self.codeName = code

    # to override a method re define in sub class
    def hello(self):
        print(f"Hello i am {self.codeName}")


Secret = SecretAgent("Scary","Terry","CodenameTerry")
Secret.reportForDuty()
Secret.hello()


## special methods

class book():
    def __init__(self,title,author,p):
        self.Title = title
        self.Author = author
        self.pages = p 
    ## Sets string representation if printed
    def __str__(self):
        return f" title = {self.Title} author = {self.Author}"

    # adds a length property
    def __len__(self):
        return self.pages

    ## overwrites the delete method
    def __del__(self):
        print( "this is the string returned when deleted b del object-name")


b = book(title = "a great book", author = "this guy",p = 9001)
print(b)
print(len(b))
del b
