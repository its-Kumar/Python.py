from threading import *
from time import sleep


class Producer:
    def __init__(self):
        self.products = []
        self.ordersplaced = False

    def produce(self):
        for i in range(1, 5):
            self.products.append("product " + str(i))
            sleep(1)
            print("Item added..")
        self.ordersplaced = True


class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        while self.prod.ordersplaced == False:
            print("Waiting..")
            sleep(0.2)

        print("Shipped  :", self.prod.products)


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
