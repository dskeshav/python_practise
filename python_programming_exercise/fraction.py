class fractions(object):
    def __init__(self,numer,denom):
        self.numer=numer
        self.denom=denom
    
    def __str__(self):
        return (str(self.numer)+"/"+str(self.denom))

    def getnumer(self):
        return self.numer

    def getdenom(self):
        return self.denom 
    def __add__(self,other):
        newNumer=other.denom*self.numer+other.numer*self.denom
        newDenom=other.denom*self.denom
        return str(newNumer)+"/"+str(newDenom)
    
    
if __name__=="__main__":
    onehalf=fractions(1,2)
    twothird=fractions(2,3)
    print(onehalf)
    print(onehalf.getnumer())
    print(fractions.getdenom(twothird))
    threequater=fractions(3,4)

    secondNew=onehalf+threequater
    print(secondNew)