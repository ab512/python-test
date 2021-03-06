#!usr/bin/env python3
# -*- coding:utf-8 -*-


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    # def user(self, name):
    #     return Chain('%s/%s/:%s' % (self._path, 'user', name))

    def __call__(self,name):
        return Chain('%s/:%s' % (self._path, name))
        

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().user('d').timeline('timeline').list)
