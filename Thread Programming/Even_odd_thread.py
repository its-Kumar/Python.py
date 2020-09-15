from threading import *


class EvenNumberThread:
    def even(self):
        print(current_thread().getName())
        for i in range(2, 100, 2):
            print(i)


class OddNumberThread:
    def odd(self):
        print(current_thread().getName())
        for i in range(1, 100, 2):
            print(i)


e = EvenNumberThread()
o = OddNumberThread()

t1 = Thread(target=e.even)
t2 = Thread(target=o.odd)

t1.start()
t2.start()
