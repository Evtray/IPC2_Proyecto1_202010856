from lists.Nodo import Nodo


class ListCell:
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

    def search(self, row, column):
        temp = self.head
        while temp != None:
            if temp.dato.getRow() == row and temp.dato.getColumn() == column:
                return temp.dato
            temp = temp.next
        return None
