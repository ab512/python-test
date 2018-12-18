# -*- coding: utf-8 -*-
import datetime
import functools
import time


def metric(func):
    @functools.wraps(func)
    def wappered(*args, **kw):
        start = datetime.datetime.now()
        result = func(*args, **kw)
        end = datetime.datetime.now()
        print('%s executed in %s ms' % (func.__name__, end-start))
        return result
    return wappered


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f=fast(11, 22)
s=slow(11, 22, 33)
print('fast func name: %s'% fast.__name__)
print('slow func name: %s'% slow.__name__)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
