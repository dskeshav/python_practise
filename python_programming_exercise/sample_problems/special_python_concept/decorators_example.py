#Decorators: Function that takes another function as an argument add some kind of functionlity 
#and then returns the other function, all that is performed is without altering the source code.

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function ran")

#display=decorator_function(display) (This is similar to above code)
display()

@decorator_function
def display_info(name,age):
    print("display_info ran with arguments({} ,{})".format(name,age))


display_info('John',25)


########################################pypt

print("##############################")
class decorator_class(object):
    def __init__(self,original_function):
        self.original_function=original_function

    def __call__(self,*args,**kwargs):
        print("call executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)



# decorator function is widely used than 
# @decorator_class
# def display_c():
#     print("display function ran")

# #display=decorator_function(display) (This is similar to above code)
# display_c()

# @decorator_class
# def display_info_c(name,age):
#     print("display_info ran with arguments({} ,{})".format(name,age))


# display_info_c('John',25)

