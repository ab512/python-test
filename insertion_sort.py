#!usr/bin/env python3
# -*- coding:utf8 -*-


def insertion_sort(a):
    if (not a) or len(a) == 0:
        return
    for j in range(1,len(a)):
        key = a[j]
        i=j-1
        while i>=0 and a[i]<key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    return a

a=[10,23,102,3223,23,5,3,6,7,3,1,2,9,0,8]

print(insertion_sort(a))

print(a)
