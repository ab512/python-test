# -*- coding:utf-8 -*-
import functools
import datetime


def log(logargs=None):
    if(logargs==None):
        logargs = ''

    def decorator(func):
        @functools.wraps(func)
        def wappered(*args, **kw):
            print('%s, %s start call' % (logargs, func.__name__))
            result = func(*args, **kw)
            print('%s, %s end call' % (logargs, func.__name__))
            return result
        return wappered
    return decorator


@log('d')
def f():
    print('do...\ndone')


f()
