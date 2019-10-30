class ListClass:
    
    def __init__(self):
        self.elements =[]
        
    def append(self,el):
        self.elements.append(el)
        
    def delete(self,el):
        self.elements.remove(el)
        
    def display(self):
        print(self.elements)
        
        
l = ListClass()
l.display()

l.append('a');    l.append('b');    l.append('c')
l.display()

l.delete('a')
l.display()

        