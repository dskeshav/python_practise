#my implementation
def row_maximums(some_multi_dimensional_list):
    row_max_dict={}
    rows_count=0
    for rows in some_multi_dimensional_list:
        row_max_dict["row {} max".format(rows_count)]=max(rows)
        rows_count+=1
    return row_max_dict

if __name__=="__main__":
    some_multi_dimensional_list=[[5, 0, 0, 0, 13],[0, 12, 0, 0],[20, 0, 11, 0],[6, 0, 0, 8]] 
    print(row_maximums(some_multi_dimensional_list))

#instructors implementation
def _max_of_each_row_sample_q5(my_multidimensional_list):
    def calculate_my_max(some_list):
        sample_max = some_list[0]
        for number in some_list:
            if number >= sample_max:
                sample_max = number

        return sample_max

    list_of_max = []
    for rows in my_multidimensional_list:
        my_max = calculate_my_max(rows)
        list_of_max.append(my_max)
    #my_sorted_list = sorted(list_of_max)
    my_dict = {}
    for x in range(0, len(list_of_max)):
        my_string = 'row' + " " +  str(x) + " " + 'max'
        my_dict[my_string] = list_of_max[x]
    
    return my_dict