from MITPerson import MITPerson
from Student import Student
class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year=classYear

    def getClass(self):
        return self.year

    def speak(self,utterance):
        return MITPerson.speak(self,'Dude,'+utterance)
