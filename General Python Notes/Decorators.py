## decoratiors allow you to call a function within another and re assign the function to the wrapped function

def hello_either_side(func):
    # a function is defined inside the decorator to use the function passed as a parameter and wrap it in extra functionality 
    # the inital function is not returned ("hello_either_side") as an inital function is required to create the wrapper

    def wrapper(*args, **kwargs): # possible params message, string , greeting -- but *args and **kwargs allow this to work for all params
        
        # parameter's passed to the original functions can be passed to the wrapping function or outer function through closure
        # the original function's arguments are live during the func being passed to the decorator or wrapper function
        # parameters are passed through a read only version of the original functions arguments and can be referenced in the decorator or wrapper
        # commonly the wrapper will accept *args & **kwargs to account for differences in functions
        # the use of args & kwargs accounts for the different params with , without and with multiple amongst the functions

        print("Hello!")
        # calling the passed function 
        # and applying optional arguments
        func(*args, **kwargs)
        print("Hello! \n\n")
    # the wrapper is then returned to give the new functionaliy and assign it to the original function
    return wrapper


# a function to be passed to the decorator function with no params
def im_going_to_be_decorated():
    print("i'm going to be decorated")

# another function for second example
def hi_middle(*args):
    print(*args)

# this shows the normal operation that is achieved with the @ syntax the original function is re assigned to the result of wrapping the original function
# PASS THE FUNCTION DO NOT INVOKE IT WHILE PASSING TO DECORATOR METHOD

##########################################

im_going_to_be_decorated = hello_either_side(im_going_to_be_decorated)
im_going_to_be_decorated()

##########################################


# the value could also be reassigned to another function name but the @ re-assigns to the same name meaning less syntax
# you can pass the function as a parameter as long as you do not invoke the function

##########################################


decorated_Without_Syntax = hello_either_side(hi_middle)
decorated_Without_Syntax("hi i'm a regular function with params")

# this can also be achieved with a lambda
decorated_Without_Syntax = hello_either_side(lambda a ,b: print(a+b))
decorated_Without_Syntax("hi im a lambda ","i also have two params")



##########################################

# decorator in use, the decorator is called and passed the function defined below it meaning the original function can be called normally
# but is then wrapped and the resulting function is assigned to the orginal function name Dec_example

@hello_either_side
def Dec_example(message):
    print(message)

Dec_example("i'm being printed with these hello's without having to manually reassign as a parameter of the hello function!")



import functools
## func tools hold wraps a additional wrapper adding a thrid layer to decorators
# the purpose of this additional layer is to preserve meta data such as __docstring__ __name__ ( the name of the original function )
# without this in the example below our function PleaseDontChangeMyName would change to WrapperNameChange

def example_decorator(func):
    @functools.wraps(func)
    ## pass function that wrap will need to gather data from
    def WrapperNameChange():
        
        func()
        print("i didn't change the name because of that wrap")

    return WrapperNameChange

@example_decorator
def PleaseDontChangeMyName():
    print(f"Hi my name is {PleaseDontChangeMyName.__name__}")

PleaseDontChangeMyName()
print(PleaseDontChangeMyName.__name__+ " \n\n")


## example with name change, the name change without wraps would occur after the decorator is ran




def example_decorator(func):
    def WrapperNameChange():
        
        func()
        print("my name changed without a wrap")

    return WrapperNameChange

@example_decorator
def MyNameWillChange():
    print(f"Hi my name is {MyNameWillChange.__name__}")

MyNameWillChange()
print(MyNameWillChange.__name__)


##### Decorators that take arguments
# decorator with arg requires additional step
# follows patter add =  decorator(args)(func)
# because of this we need to add an additional layer of wrapping

def ensureSumIsTen(val):
# when reaching this line the  function will be passed 10 and called

    def inner(func):
        # function is passed as the __call__ method is triggered and @ passes the function numbers in as an argument
        # like so ensureSumIsTen(10) = inner(numbersin) the call method allows us to specify what we pass in as we call the function
        # in this instance we give it the decorated function __call__(NumbersIn):
        #   wrapper():
        #       numbersin()
        def wrapper(*args,**kwargs):
            if args and func(*args) == val:
                return("you pass")
            elif kwargs:
                return("kwargs, very sneaky")
            else :
                return "Fail"
        return wrapper
    return inner


@ensureSumIsTen(10)

def numbersIn(a,b):
    return   a+b

print(numbersIn(5,5))