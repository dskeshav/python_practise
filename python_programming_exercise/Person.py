# class Person():
#     pass

# person=Person()

# # person.first='Corey'
# # person.last="Schafer"

# # print(person.first)
# # print(person.last)
# first_key='first'
# first_val='Corey'

# # person.first_key=first_val
# setattr(person,first_key,first_val)

# first=getattr(person,first_key)
# print(first)
# person_info={'first':"Corey",'last':'Schafer'}

# for key,value in person_info.items():
#     setattr(person,key,value)


# for key in person_info.keys():
#     print(getattr(person,key))

from getpass import getpass
username=input('Username: ')
password=getpass('Password ',stream='$')

print('Logging In...')