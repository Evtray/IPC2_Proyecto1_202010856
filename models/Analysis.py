from operator import index


class Analysis:
    def __init__(self, indexPatiente, pattern, cells, period, sizeCells):
        self.indexPatiente = indexPatiente
        self.pattern = pattern
        self.cells = cells
        self.period = period
        self.sizeCells = sizeCells

    def getIndexPatiente(self):
        return self.indexPatiente

    def getPattern(self):
        return self.pattern
    
    def getCells(self):
        return self.cells
    
    def getPeriod(self):
        return self.period
    
    def getSizeCells(self):
        return self.sizeCells
    
    def setIndexPatiente(self, indexPatiente):
        self.indexPatiente = indexPatiente

    def setPattern(self, pattern):
        self.pattern = pattern
    
    def setCells(self, cells):
        self.cells = cells
    
    def setPeriod(self, period):
        self.period = period
    
    def setSizeCells(self, sizeCells):
        self.sizeCells = sizeCells
