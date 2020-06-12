class Duck:

    def talk(self):
        print("Quack Quack...")


class Human:

    def talk(self):
        print("Hello...")


def CallTalk(obj):
    obj.talk()


d = Duck()
CallTalk(d)

h = Human()
CallTalk(h)
