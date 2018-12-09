# -*- coding: utf-8 -*-
def _by_name(x):
    return x[0].lower()


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

orderTuple = sorted(L, key=_by_name)
print(_by_name)
print(orderTuple)