vowels=['a','e','i','o','u']
word=input("Provide a word to search for vowels: ")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)


# fo=open("C:\\Users\\dkeshav\\Desktop\\Resolve_Note.docx","r+")
# print("Name of the file :", fo.name)
# fo.read(10)
# print("Name of the file 1:", fo.tell())


# numList=[]
# size=int(input("Enter number of elements to be inserted into the list: "))
# for counter in range(0,size):
#     b=int(input("Enter element:"))
#     numList.append(b)
# numList.sort()
# print(numList)
# print(numList[-1])



# n=int(input("Enter upper limit of range: "))
# sieve=set(range(2,n+1))
# while sieve:
#     prime=min(sieve)
#     print(prime,end="\t")
#     sieve-=set(range(prime,n+1,prime))
 
# print()




# n=int(input("Enter the number: "))

# temp=str(n)
# t1=temp+temp
# t2=temp+temp+temp
# comp=n+int(t1)+int(t2)
# print("The value is: ",comp)

# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# num3=int(input("Enter the third number: "))
# d=[]
# d.append(num1)
# d.append(num2)
# d.append(num3)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if(i!=j & j!=k & k!=i):
#                 print(d[i],d[j],d[k])



# nondivisible=[]
# for counter in range(1,51):
#     if((counter%2 !=0) & (counter%3 !=0)):
#         nondivisible.append(counter)

# print(nondivisible)


# n=int(input("Enter a number: "))
# a=[]
# for i in range(1,n+1):
#     print(i,sep=" ",end=" ")
#     if(i<n):
#         print("+",sep=" ",end=" ")
#     a.append(i)
# print("=",sum(a))
 
# print()

# n=int(input("Enter number of rows: "))
# for i in range(n,0,-1):
#     print((n-i)*' '+i*'* ')


      