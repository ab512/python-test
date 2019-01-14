import threading

shool_local = threading.local()


def process_student():
    name = shool_local.student_name
    print('student name: %s(theard is %s)' % (name,  threading.current_thread().name))


def process_thread(name):
    shool_local.student_name=name
    process_student()

thread1=threading.Thread(target=process_thread, args=("abc",), name="thread-1")
thread2=threading.Thread(target=process_thread, args=("efg",), name="thread-2")

thread1.start()
thread2.start()
thread1.join()
thread2.join()
