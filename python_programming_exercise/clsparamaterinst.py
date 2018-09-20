class Person:
    # define class parameter name
    name="Person"

    def __init__(self, name=None):
        #self.name is a instance paramater
        self.name=name

    
jeffery=Person("Jeffery")

print("%s name is %s" % (Person.name,jeffery.name))

nico=Person()

print("%s name is %s" % (Person.name,nico.name))