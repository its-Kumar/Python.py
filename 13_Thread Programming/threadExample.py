from threading import Lock, Thread


class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.lock = Lock()

    def buy(self, seatsReq):
        print("Total seat available : ", self.availableSeats)
        self.lock.acquire()
        if self.availableSeats >= seatsReq:
            print("Confirming the seat..")
            print("Processing the payment..")
            print("Printing the ticket.")
            self.availableSeats -= seatsReq
        else:
            print("Sorry. No seats available...")
        self.lock.release()


obj = BookMyBus(10)
t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(5,))
t3 = Thread(target=obj.buy, args=(3,))

t1.start()
t2.start()
t3.start()
