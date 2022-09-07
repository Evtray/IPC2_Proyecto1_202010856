from lists.Nodo import Nodo

class ListAnalysis:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, cell):
        new = Nodo(cell) 

        if self.head == None:
            self.head = new
            self.last = new
        else:
            self.last.siguiente = new
            self.last = new

    def searchPattern(self, pattern):
        temp = self.head
        count = 0
        while temp != None:
            if temp.dato.getPattern() == pattern:
                count += 1
            temp = temp.next
        return count