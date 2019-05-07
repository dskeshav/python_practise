from UG import UG
from Grad import Grad
from Student import Student

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Creates empty grade book"""
        self.students=[]
        self.grades={}
        self.isSorted=True

    def addStudent(self,student):
        """ Assumes: student is of type student
            Add student to the grade book."""
        if student in self.students:
            raise ValueError('Duplicate Error')
        self.students.append(student)
        self.grades[student.getIdNum()] =[]
        self.isSorted=False

    def addGrades(self,student,grade):
        """Assumes: grade is float
            Add grades to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def getGrades(self,student):
        """Return a list of grades for a student"""
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """ Return a list of the students in thew grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted=True
        #return copy of list of students
        for s in self.students:
            yield s

    def gradeReport(self,course):
        """Assumes: course is of type grades"""
        report=[]
        for s in course.allStudents():
            tot=0.0
            numGrades=0
            for g in course.getGrades(s):
                tot+=g
                numGrades+=1
            try:
                average=tot/numGrades
                report.append(str(s)+'\'s mean grade is '+str(average)) 

            except ZeroDivisionError:
                report.append(str(s)+ ' has no grades')
        return "\n".join(report)


# s1=Student('Matt Damon',2018)
# s2=Student('Ben Affleck',2019)
# s3=Student('Drew Houston',2017)
# s4=Student('Mark Zuckerberg',2017)

ug1=UG('Matt Damon',2018)
ug2=UG('Ben Affleck',2019)
ug3=UG('Drew Houston',2017)
ug4=UG('Mark Zuckerberg',2017)
g1=Grad('Bill Gates')
g2=Grad('Steve Wozniak')

six00=Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrades(g1,100)
six00.addGrades(g2,25)
six00.addGrades(ug1,95)
six00.addGrades(ug2,85)
six00.addGrades(ug3,75)

print(six00.gradeReport(six00))