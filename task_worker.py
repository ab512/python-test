import time
import sys
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

serverAddress = '127.0.0.1'
port = 5000

manager = QueueManager(address=(serverAddress, port), authkey=b'abc')

manager.connect()

tasks = manager.get_task_queue()
results = manager.get_result_queue()

for i in range(10):
    try:
        n = tasks.get()
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        results.put(r)
    except Queue.Empty:
        print('queue is empty.')
print('worker exit.')