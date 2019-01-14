import os
print('Process %s is start...' % os.getppid())
pid = os.fork()
if pid == 0:
    print('I am chirlden process %s and my parent process is %s' %
          (os.getpid(), os.getppid()))
else:
    print('I am %s create a chirlden process %s' % (os.getpid(), pid))
