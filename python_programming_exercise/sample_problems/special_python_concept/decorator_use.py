#Common use case of decorator is logging
#Used for class problem 
#Used for routing
#web framework

from functools import wraps

def my_logger(orgi_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orgi_func.__name__),level=logging.INFO)

    @wraps(orgi_func)
    def wrapper(*args,**kwargs):
        logging.info("Ran with args: {},and kwargs:{} ".format(args,kwargs))
        return orgi_func(*args,**kwargs)
    return wrapper

def my_timer(orgi_func):
    import time
    
    @wraps(orgi_func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=orgi_func(*args,**kwargs)
        t2=time.time() -t1
        print("{} ran in : {} sec".format(orgi_func.__name__,t2))
        return result
    return wrapper

# @my_logger
# def display_info(name,age):
#     print("display_info ran with arguments({} ,{})".format(name,age))


# import time

# @my_timer
# def display_info(name,age):
#     time.sleep(1)
#     print("display_info ran with arguments({} ,{})".format(name,age))

# display_info("Hank",30)
import time

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print("display_info ran with arguments({} ,{})".format(name,age))

display_info("Tom",22)