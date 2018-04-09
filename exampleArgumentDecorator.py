class decoratorWithArguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        # the function is called with the given decorator arguments and saves them in the object
        print ("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        # when the decorator is initalised it is passed the function below through decoratorwitharguments __call__(self SayHello)
        # this is then wrapped up as below and this then forms the new call method
        # when the decorated method is then called the inner wrapped function is the __call__method due to the above re assignment and is given
        # scope to see the arguments through the objects earlier save
        print ("Inside __call__()")
        def wrapped_f(*args):
            print ( "Inside wrapped_f()")
            print ("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print ("After f(*args)")
        return wrapped_f

@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print ('sayHello arguments:', a1, a2, a3, a4)

print ("After decoration")

print ("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print ("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print ("after second sayHello() call")