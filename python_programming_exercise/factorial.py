""" Program to find factorial of a number"""

def fact(x):
    f=1 
    while(x!=0):
        f*=x
        x=x-1
    return f
def main():
    print("Enter a valid number to compute a factorial of a number")
    try:
         x=int(input())
         print(fact(x))
    except ValueError:
        print('Invalid entry')
        main()
        

main()

