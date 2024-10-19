class Father:
    def gardening(self):
        print("I enjoy gardening")

    def skills(self):
        print("gardening, programming")


class Mother:
    def cooking(self):
        print("I love cooking.")

    def skills(self):
        print("cooking, music")


class Child(Father, Mother):
    def sports(self):
        print("I enjoy sporting.")

    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")


if __name__ == "__main__":
    c = Child()
    c.gardening()
    c.cooking()
    c.sports()
    c.skills()
