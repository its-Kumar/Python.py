from threading import Thread


class MyThread(Thread):
    def run(self):
        i = 0
        while (i <= 10):
            print(i)
            i += 1


t = MyThread()
t.start()
