class Duck:
    def talk(self):
        print("Quack Quack...")


class Human:
    def talk(self):
        print("Hello...")


def call_talk(obj):
    obj.talk()


d = Duck()
call_talk(d)

h = Human()
call_talk(h)
