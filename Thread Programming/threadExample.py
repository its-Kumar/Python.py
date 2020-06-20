from threading import *


class BookMyBus:

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Lock()

    def buy(self, seatsReq):
        print("Total seat available : ", self.availableSeats)
        self.l.acquire()
        if (self.availableSeats >= seatsReq):
            print("Confirming the seat..")
            print("Processing the payment..")
            print("Printing the ticket.")
            self.availableSeats -= seatsReq
        else:
            print("Sorry. No seats available...")
        self.l.release()


obj = BookMyBus(10)
t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(5,))
t3 = Thread(target=obj.buy, args=(3,))

t1.start()
t2.start()
t3.start()
