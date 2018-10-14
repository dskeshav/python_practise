import datetime

class Person(object):
    def __init__(self,name):
        """Create a person called name"""
        self.name=name
        self.birthday=None
        self.lastName=name.split(' ')[-1]

    def getLastName(self):
        return self.lastName

    def setBirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)
    
    def getAge(self):
        if self.birthday==None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        """return True if slef's name is lexicographically 
        less than other's name, and False otherwise""" 
        if self.lastName== other.lastName:
            return self.name<other.name
        return self.lastName<other.lastName

    def __str__(self):
        """return self's name"""
        return self.name



# p1=Person('Mark Zuckerberg')
# p1.setBirthday(5,14,84)
# p2= Person('Bill Gates')
# p2.setBirthday(10,28,55)
# p3=Person('Drew Houston')
# p3.setBirthday(3,4,83)
# p4=Person('Andrew Gates')
# p5=Person('Steve Wozniak')

# personList=[p1,p2,p3,p4,p5]

# print(p1)
# print('\n')
# personList.sort()
# for e in personList:
#     print(e)
# print('p1<p4: ',p1<p4)


class TransferStudent(Student):
    pass
def isStudent(obj):
    return isinstance(obj,Student)






