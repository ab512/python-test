#!usr/bin/env python3
# -*- coding:utf-8 -*-


class test(object):
    pass


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(dict, metaclass = ListMetaclass):
    def append(self, v):
        self[v] = v


L = MyList()
L.add('2')
print(L)
