#!usr/bin/env python3
# -*- coding:utf-8 -*-


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if(self.a > 10000):
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        elif isinstance(n, slice):
            a, b = 1, 1
            if n.start == None:
                n.start = 0
            step = 1
            if n.step != None:
                step = n.step
            if n.step == 0:
                raise TypeError('slice step cannot be zero')
            L = list()
            index = 0
            for x in range(n.stop):
                if x >= n.start and index % step == 0:
                    L.append(a)

                if x >= n.start:
                    index += 1
                a, b = b, a+b

            return L


fib = Fib()
for item in fib:
    print(item)

print(fib[0])
print(fib[1])
print(fib[2])
print(fib[3])
print(fib[100])
print(fib[5:10:5])