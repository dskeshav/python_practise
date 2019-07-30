
def funcEval(fnum):
    n=fnum-2
    if fnum in fvalue.keys():
        return fvalue.get(fnum)
    elif fnum%2==0 and n>2:
        result1= 2*funcEval(n+1)-funcEval(n)+2
        fvalue.update({fnum: result1})
        return result1
    elif fnum%2!=0 and n>2:
        result2= 3*funcEval(n)
        fvalue.update({fnum:result2})
        return result2

T,P=map(int,input().split(' '))
fvalue={1:1,2:1}

for loop in range(T):
    L,R=map(int,input().split())
    sum=0
    for fnum in range(L,R+1,1):
        # print("fnum: ",fnum)
        sum+=funcEval(fnum)
    print(sum%P)

