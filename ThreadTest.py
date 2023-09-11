from threading import Thread
from myTask import myTask

t1 = Thread(target=myTask)
t2 = Thread(target=myTask)
t3 = Thread(target=myTask)
t1.start()
print('t1 started')
t2.start()
print('t2 started')
t3.start()
print('t3 started')
t1.join()
t2.join()
t3.join()