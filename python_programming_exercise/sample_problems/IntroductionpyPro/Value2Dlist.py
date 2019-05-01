import datetime

def maxeven(num_list):
    t0=datetime.datetime.now()
    if not num_list:
        return None
    max_even_num=0
    print(max_even_num)
    odd_occurance=0
    list_element_count=0
    for outer in num_list)):
        for inner in range(0,len(num_list[outer])):
            list_element_count+=1
            if num_list[outer][inner]%2 !=0:
                odd_occurance+=1
            else:
                print(max_even_num, ': ',num_list[outer][inner])
                if max_even_num<num_list[outer][inner]:
                    max_even_num=num_list[outer][inner]
                    print("inside loop:",max_even_num, ': ',num_list[outer][inner] )
            
    if odd_occurance==list_element_count:
        return None
    t1=datetime.datetime.now()
    print("maxeven time for execution: ",t1-t0)
    return max_even_num


def _maximum_even_value_sample_(num_list):
    t0=datetime.datetime.now()
    if not num_list: # list is empty
        return None
    result=None
    for row in num_list:
        row_max=_max_even_of_1d_list(row)
        if row_max:
            if result==None or row_max>result:
                result=row_max
    t1=datetime.datetime.now()
    print("maximum_even_sample: ",t1-t0)
    return result

def _max_even_of_1d_list(input_list):
    result=None
    for element in input_list:
        if element%2 ==0: # if element is even
            if result==None or element>result:
                result=element
    return result


if __name__=="__main__":
    num_list=[[1, 3, 3, 5], [1, 5, 3, 5],[11,5,9,15],[7,13,51,5],[3,1,1,9]]
    print(maxeven(num_list))
    print(_maximum_even_value_sample_(num_list))
    