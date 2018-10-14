# def square_num(nums):
#     for i in nums:
#         yield (i*i)


# def main():
#     # my_nums=square_num([1,2,3,4,5])
#     my_nums=(x*x for x in [1,2,3,4,5])

#     print(list(my_nums))

#     # for num in my_nums:
#     #     print(num) 


# if __name__=='__main__':
#     main()


import mem_profile
import random
import time

names=['John','Corey','Adam','Steve','Rick','Thomas']
majors=['Math','Engineering','CompSci','Arts','Business']

# print('Memory (Before):{}Mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    result=[]
    for i range(num_people):
        person={
                'id':i,
                'name':random.choice(names)
                'major':random.choice(majors)
               }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person={
                'id':i,
                'name':random.choice(name)
                'major':random.choice(majors)
                }
        yield person