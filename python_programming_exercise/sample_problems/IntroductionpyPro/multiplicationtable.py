def multiplication_table(n):
    multiply_list=[]
    for row in range(1,n+1):
        row_list=[]
        for column in range(1,n+1):
            row_list.append(column*row)
        multiply_list.append(row_list)
    return multiply_list

if __name__=="__main__":
    print(multiplication_table(10))
