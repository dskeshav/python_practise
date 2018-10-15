from MITPerson import MITPerson

class Student(MITPerson):
    pass

s1=UG('Matt Damon',2017)
s2=UG('Ben Afflex',2017)
s3=UG('Lin Manuel Miranda',2018)
s4=Grad('Leonardo di Caprio')

studentList=[s1,s2,s3,s4]

print('student ::')
print()

print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no idea!'))
   
