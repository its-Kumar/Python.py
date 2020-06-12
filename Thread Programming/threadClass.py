from threading import *
from time import sleep


class MyThread:
    def DisplayNumbers(self):
        i = 0
        print(current_thread().getName())
        sleep(1)
        while(i <= 10):
            i += 1
            print(i)


obj = MyThread()
t1 = Thread(target=obj.DisplayNumbers)
t1.start()

t2 = Thread(target=obj.DisplayNumbers)
t2.start()

t3 = Thread(target=obj.DisplayNumbers)
t3.start()

t4 = Thread(target=obj.DisplayNumbers)
t4.start()
