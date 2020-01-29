class LinkedList:
    def __init__(self):
        self.elements =[]

    def is_empty(self):
        return self.elements == []

    def insert(self,item):
        self.elements.append(item)

    def insert_atstart(self,item):
        self.elements.insert(0,item)

    def  delete(self,item):
        if self.is_empty():
            print("Linked list is Empty...")
        self.elements.remove(item)

    def delete_position(self,position):
        if self.is_empty():
            print("Linked list is Empty...")
        self.elements.pop(position - 1)
    def display(self):
        print(self.elements)



l = LinkedList()
while True:
    print("Linked List : ")
    print("1. Insert\n2. Insert at start \n3. Delete \n4. Delete by position\n5. Display ")
    ch = int(input("Enter your choice : "))
    if ch ==1:
        item = input("Enter item : ")
        l.insert(item)
    elif ch ==2:
        item = input("Enter item : ")
        l.insert_atstart(item)
    elif ch==3:
        item = input("Enter item : ")
        l.delete(item)
    elif ch ==4:
        position = int (input("Enter position : "))
        l.delete_position(position)

    else:
        l.display()

