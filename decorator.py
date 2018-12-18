#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'cy'


import functools


def log(func):
    @functools.wraps(func)
    def wrappersdsd(*args, **kw):
        print('call %s():' % func.__name__)
        print('args:%s', args)
        return func(*args, **kw)
    return wrappersdsd


@log
def now():
    print('111222')


now()

print(now.__name__)
