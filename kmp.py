#!usr/env/bin python3
# -*- coding:utf-8 -*-


def failsuit(str):
    str_length = len(str)
    index = 1
    fail_suit_index_list = list()
    fail_suit_index_list.append(-1)
    while index < str_length:
        j = fail_suit_index_list[index-1]
        print('big %s',j)
        while True:
            if(str[j+1] == str[index]):
                fail_suit_index_list.append(j+1)
                break
            elif j == -1:
                fail_suit_index_list.append(-1)
                break
            j = fail_suit_index_list[j]
            print('small %s',j)
        index += 1
    print(fail_suit_index_list)
    return fail_suit_index_list


def failsuitf(str):
    str_length = len(str)
    index = 1
    fail_suit_index_list = list()
    fail_suit_index_list.append(-1)
    while index < str_length:
        j = fail_suit_index_list[index-1]+1
        if(str[j] == str[index]):
            fail_suit_index_list.append(j)
        else:
            fail_suit_index_list.append(-1)
        index += 1
    print(fail_suit_index_list)
    return fail_suit_index_list


def next(str):
    fail_next_list = list()
    temp_fail_list = failsuit(str)
    for item in temp_fail_list:
        fail_next_list.append(item+1)
    return fail_next_list


print(next("ababaaabdsfdsfs"))
