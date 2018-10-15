# class Shape(object):
#     def __init__(self):
#         pass

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self,length):
#         self.length=length

#     def area(self):
#         return self.length**2


# aSquare=Square(3)
# print(aSquare.area())


def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("zero division error")
except Exception:
    print("Exception")
finally:
    print("In the finally block of the Exception")
    