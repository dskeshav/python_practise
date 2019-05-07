# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address. 
# Both user names and company names are composed of letters only.


import re

def emailMatch():
    emailAddress="john1@teksystems.com"
    part2="(\w+)@((\w+\.)+(com))"
    r2=re.match(part2,emailAddress)
    print(r2.group(2))
    return 0

def findallMethod():
    #a program which accepts a sequence of words separated
    #by whitespace as input to print the words composed of digits only.
    string="2 dogs 3.0 cats"
    print(re.findall("\d",string))
    return 0


if __name__=='__main__':
    emailMatch()
    findallMethod()