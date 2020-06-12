class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class AeroEngine:
    def start(self):
        print("Starting Aero Engine..")


class BritoEngine:

    def start(self):
        print("Starting the Brito Engine..")


ae = AeroEngine()
f1 = Flight(ae)
f1.startEngine()

be = BritoEngine()
f2 = Flight(be)
f2.startEngine()
