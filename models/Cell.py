class Cell:
    def __init__(self,row, column):
        self.row  = row 
        self.column = column

    # def getters and setters
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def setRow(self, row):
        self.row = row
    
    def setColumn(self, column):
        self.column = column