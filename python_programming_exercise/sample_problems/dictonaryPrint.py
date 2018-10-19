# program to generate a dictionary that contains 
# (i, i*i) such that is an integral number between 1 and n (both included).

print("Enter a number whose dictonary is to be created")
n=range(int(input()))
dictonary={str(i):i**2 for i in n}
print(dictonary)
print(type(dictonary))