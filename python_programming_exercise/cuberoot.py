x=int(input("Enter an integer: "))
ans=0
while ans**3<abs(x):
    ans +=1

if ans**3 !=abs(x):
    print("Integer "+ str(x) + " is not a perfect cuberoot number")
else:
    print("Integer "+ str(x) + " is a perfect cuberoot number and its cuberoot is "+ str(ans))