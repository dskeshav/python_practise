# # abs()
# print("absolute value of -10 is :",abs(-10))

# print("absolute value of 10.53 is :",abs(10.530))

# print("absolute value of complex number is :",abs(complex(2,2)))

# #all()
# def all(iterable):
#     for element in iterable:
#         if  not element:
#             return False
#     return True

# listIterate={1}
# print("all elements of the list are iterable: ",all(listIterate))


# #bin()
# print("Binary representation of 5 :",bin(5))


# #bool
# print("bool example:",bool())

# #bytearray
# rlist=[1,2,2]
# arr=bytearray(rlist)
# print("Bytearray :",arr)


# size=5
# ar1=bytearray(size)
# print("bytearray(size):",ar1)

# string="Python is interesting"
# ar2=bytearray(string,'utf-8')
# print(ar2)

# print("bytearray() i.e no arguments: creates the bytearray of 0 size: ",bytearray())


# #callable()
# x=10
# print(callable(x))


# #@classmethods
# class Person:
#     age=25

#     def printAge(cls):
#         print("The age is : ", cls.age)
    
# #create printAge class method
# Person.printAge=classmethod(Person.printAge)

# Person.printAge()


# def testfunction():
#     print("Test")
# y=testfunction
# print(callable(y))

# print(dir())

# #enumerate
# print(set)
# seasons=['summer','rainy','winter']
# print(list(enumerate(seasons)))


# #dict
# numbers1=dict(x=5,y=6)
# print("dict: numbers1",numbers1)

# numbers2=dict([('x',4),('y',8)])
# print("dict: numbers2",numbers2)

# numbers3=dict()


# #map()
# def squares(n):
#     return n*n

# numlist=[1,2,3,4,5]

# result=map(squares,numlist)
# print("squares of numbers set",result)

# numsquares=set(result)

# print(numsquares)

# result1=set(map(squares,numlist))
# result2=list(map(squares,numlist))

# print("squares of numbers set: result 1:",result1)
# print("squares of numbers list: result 2:",result2)


# #map() with lambda function
# lambdaresult =list(map(lambda n:(n*n),numlist))
# print("map with lambda function:",lambdaresult)

# #map() with lambda and multiple iterator
# n1=[1,2,3]
# n2=[4,5,6]
# lambdamultiterator=list(map(lambda n1,n2:n1+n2,n1,n2))
# print("map with lambda and multiple iterator: ",lambdamultiterator) 


# #locals()
# print("locals",locals())

# #min()
# print("min(): ", min(lambdamultiterator))


# #divmod()
# print("divmod(): ",divmod(10,3))


# #random bytearray
# randomByteArray = bytearray('ABC', 'utf-8')

# mv = memoryview(randomByteArray)

# # access memory view's zeroth index
# print(mv[0])

# # create byte from memory view
# print(bytes(mv[0:2]))

# # create list from memory view
# print(list(mv[0:3]))

# import sys, math

# def hash_fraction(m, n):
#     """Compute the hash of a rational number m / n.

#     Assumes m and n are integers, with n positive.
#     Equivalent to hash(fractions.Fraction(m, n)).

#     """
#     P = sys.hash_info.modulus
#     # Remove common factors of P.  (Unnecessary if m and n already coprime.)
#     while m % P == n % P == 0:
#         m, n = m // P, n // P

#     if n % P == 0:
#         hash_value = sys.hash_info.inf
#     else:
#         # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
#         # pow(n, P-2, P) gives the inverse of n modulo P.
#         hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
#     if m < 0:
#         hash_value = -hash_value
#     if hash_value == -1:
#         hash_value = -2
#     return hash_value

# def hash_float(x):
#     """Compute the hash of a float x."""

#     if math.isnan(x):
#         return sys.hash_info.nan
#     elif math.isinf(x):
#         return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
#     else:
#         return hash_fraction(*x.as_integer_ratio())

# def hash_complex(z):
#     """Compute the hash of a complex number z."""

#     hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
#     # do a signed reduction modulo 2**sys.hash_info.width
#     M = 2**(sys.hash_info.width - 1)
#     hash_value = (hash_value & (M - 1)) - (hash_value & M)
#     if hash_value == -1:
#         hash_value = -2
#     return hash_value

# print(hash_fraction(3,2))
# print(hash_float(3.2))
# print(hash_complex(3))
