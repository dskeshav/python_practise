# Hacking Python’s memory with __slots__

import collections
import datetime

ImmutableThingTuple = collections.namedtuple('ImmutableThingTuple','a b c d')

class MutableThing:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

class ImmutableThing:
    __slots__=['a','b','c','d']

    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

print("Uncomment exactly 1 of the 4 loops below")
print("after the program pauses on the input, check the process memory")

count=10000
data=[]

t0=datetime.datetime.now()

#Loop 1: tuples

# print("tuple")
# for n in range(count):
#     data.append((1+n,2+n,3+n,4+n))

# #Loop 2: Named Tuples
# print("Named Tuples")
# for n in range(count):
#     data.append(ImmutableThingTuple(1+n,2+n,3+n,4+n))

# #Loop 3: Standard mutable class
# print("Standard mutable class")
# for n in range(count):
#     data.append(MutableThing(1+n,2+n,3+n,4+n))  

# #Loop 4: Slot based immutable class
print("Slot based immutable class")
for n in range(count):
    data.append(ImmutableThing(1+n,2+n,3+n,4+n))

t1=datetime.datetime.now()

input("Finished, wating... done in {:,} s".format((t1-t0).total_seconds()))