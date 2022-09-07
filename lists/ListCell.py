from lists.Nodo import Nodo
from models.Cell import Cell


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
            self.last.next = new
            self.last = new

    def analize(self, size):
        cells = ListCell()
        pattern = ''
        for i in range(1, size + 1):
            for x in range(1, size + 1):
                cell = self.searchCell(i, x)
                countCells = 0

                countCells += self.searchCell( i-1, x-1)
                countCells += self.searchCell( i-1, x)
                countCells += self.searchCell( i-1, x+1)

                countCells += self.searchCell( i, x+1)
                countCells += self.searchCell( i, x-1)

                countCells += self.searchCell( i+1, x-1)
                countCells += self.searchCell( i+1, x)
                countCells += self.searchCell( i+1, x+1)

                index = '0'
                if cell == 1:
                   if countCells in [2,3]:
                        index = '1'
                if cell == 0:
                    if countCells == 3:
                        index = '1'
            
                pattern += index
                if index == '1':
                    cell = Cell(i, x)
                    cells.insert(cell)
        
        return {'pattern': pattern, 'cells': cells}

    def searchCell(self, row, column):
        temp = self.head
        while temp != None:
            if temp.dato.getRow() == row and temp.dato.getColumn() == column:
                return 1
            temp = temp.next
        return 0
