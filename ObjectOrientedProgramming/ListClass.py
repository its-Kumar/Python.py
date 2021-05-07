class ListClass:
    def __init__(self):
        self.elements = []

    def append(self, el):
        self.elements.append(el)

    def delete(self, el):
        self.elements.remove(el)

    def display(self):
        print(self.elements)


lst = ListClass()
lst.display()

lst.append("a")
lst.append("b")
lst.append("c")
lst.display()

lst.delete("a")
lst.display()
