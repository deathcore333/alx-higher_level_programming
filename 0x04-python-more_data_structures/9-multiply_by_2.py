#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()

    for key in new_dic:
        new_dic[key] = new_dic[key] * 2
    return new_dic
