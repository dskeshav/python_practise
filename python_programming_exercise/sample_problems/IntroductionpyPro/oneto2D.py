def one_to_2D(some_list, r, c):
    _2Dlist=[]
    length=len(some_list)
    product=r*c
    if length>product:
        some_list=some_list[0:product]
    else:
        for _ in range(length,product):
            some_list.append(None)
    
    for i in range(0,len(some_list),c):
        _2Dlist.append(some_list[i:i+c])

    return _2Dlist


if __name__=="__main__":
    print(one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10,11,12,13,14], 3, 4)) 
        