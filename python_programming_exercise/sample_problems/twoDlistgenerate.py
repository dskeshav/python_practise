# program which takes 2 digits, X, Y as input and generates a 2-dimensional array.
#  The element value in the i-th row and j-th column of the array should be i*j.

def  computeA():
    print()
    print("Enter a number such that sum of 'a+aa+aaa+aaaa' will be computed")
    
    try:
        a=int(input())
        n1 = int( "%s" % a )
        n2 = int( "%s%s" % (a,a) )
        n3 = int( "%s%s%s" % (a,a,a) )
        n4 = int( "%s%s%s%s" % (a,a,a,a) )
        print (n1+n2+n3+n4)

    except ValueError:
        print("Invalid entry")
        computeA()


def printstrupper():
    print("Type sentences in multiple lines")
    lines=[]
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break
    for sentence in lines:
        print(sentence)
    
#program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    computeA()        


def main():
    print("Enter size of matrix")
    size=input()
    dimensions=size.split(",")
    if len(dimensions)==2:
        numRow=int(dimensions[0])
        numCol=int(dimensions[1])
        print(numRow," ",numCol)
        twoDlist=[[(row*col) for col in range(numCol) ]for row in range(numRow)]
    print(twoDlist)   
    

    #a program that accepts sequence of lines as input and
    #prints the lines after making all characters in the sentence capitalized.
    printstrupper()

main()

