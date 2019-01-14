#!usr/bin/env python3
# -*- coding:utf-8 -*_


from multiprocessing import Process, Queue
import os
import random
import time


def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(r):
    print('Process to read: %s' % os.getpid())
    while True:
        value = r.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()

    time.sleep(1)
    pr.terminate()

