def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    construct_dict={}
    for index in range(len(names_list)):
        if scores_list[index]>=60:
            construct_dict[names_list[index]]=[ages_list[index],scores_list[index],'pass']
        else:
            construct_dict[names_list[index]]=[ages_list[index],scores_list[index],'fail']
    return construct_dict

if __name__=="__main__":
    ages_list=[28, 59, 22, 5]
    scores_list=[59, 85, 55, 60]
    names_list=["paul", "saul", "steve", "chimpy"]
    dictionary=construct_dictionary_from_lists(names_list, ages_list, scores_list)
    print(dictionary)