from threading import *


def DisplayNumbers():
    i = 0
    print(current_thread().getName())
    while(i <= 10):
        i += 1
        print(i)


print(current_thread().getName())
t = Thread(target=DisplayNumbers)
t.start()
