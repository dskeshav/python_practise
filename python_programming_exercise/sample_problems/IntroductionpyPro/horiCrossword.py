# # Type your code here 
# def find_word_horizontal(crosswords,word):
#     print(len(crosswords[0]),len(word))
#     for row in crosswords:
#         print(row)
#         words_list=[]

def find_word_horizontal(crosswords,word):
    if not crosswords or not word : # if empty then return None
        return None
    for index,row in enumerate(crosswords):
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None

def find_word_vertical(crosswords,word):
    if not crosswords or not word :
        return None
    number_of_columns=len(crosswords[0]) 
    for num_colums in range(number_of_columns):
        temp_str=""
        for num_rows in range(len(crosswords)):
            temp_str.join(crosswords[num_rows][num_colums])
        if temp_str.find(word)>=0:
            return [temp_str.find(word),num_colums]


if __name__=="__main__":
    crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
    word='cat'
    print(find_word_horizontal(crosswords,word))