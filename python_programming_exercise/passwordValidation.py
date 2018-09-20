#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
import re

def main():
    print("Type set of password:")
    print('''Password must contain :
    1.At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12''')
    passString=input()
    passwords=passString.split(",")
    value=[]
    for passw in passwords:
        if len(passw)<6 or len(passw)>12:
            print("Inside len",passw)
            continue 
        else:
            print("Inside pass of len")
            pass
        
        if not (re.search("a-z",passw) and re.search(0-9,passw) and re.search("$#@",passw)
                    and re.search("A-Z",passw)):
            print("inside check block of character",passw)        
            continue
        else:
            pass

        value.append(passw)
        print("print value",value)


    print(",".join(value))
        

main()