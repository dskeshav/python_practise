import datetime
import sys

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)


def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib_efficient(n-1,d)+fib_efficient(n-2,d)
        d[n]=ans
        return ans

def main():
    N=int(input("Enter the number : "))
    
    print("fib inefficient")
    t0=datetime.datetime.now()
    print(fib(N))
    t1=datetime.datetime.now()

    print("inefficient time: ",(t1-t0).total_seconds())
    sys.stdout.flush()
    d={1:1,2:2}
    print('fib efficient')
    t2=datetime.datetime.now()
    print(fib_efficient(N,d))
    t3=datetime.datetime.now()
    print("efficient time: ",(t3-t2).total_seconds())


if __name__=="__main__":
    main()