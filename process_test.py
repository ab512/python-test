from multiprocessing import Process
import os


def process_run(name):
    print('run process %s name:%s' % (os.getpid(), name))


if __name__ == '__main__':
    print('run main %s name %s' % (os.getpid(), os.name))
    p = Process(target=process_run, args=("test",), name='test-process-first')
    print('run start child process %s,%s' % (p.name,p.pid))
    p.start()
    p.join()
    print('child process end')
