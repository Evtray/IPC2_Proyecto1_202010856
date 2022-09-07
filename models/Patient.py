from models.Analysis import Analysis


class Patient:
    def __init__(self, name, age, periods, size, cells, index):
        self.name = name
        self.age = age
        self.periods = periods
        self.cells = cells
        self.size = size
        self.analysis = None
        self.result = None
        self.index = index
    
    def analyze(self):
        pass
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getPeriods(self):
        return self.periods
    
    def getSize(self):
        return self.sizeCells
    
    def getCells(self):
        return self.cells
    
    def getAnalysis(self):
        return self.analysis
    
    def getResult(self):
        return self.result

    def getIndex(self):
        return self.index
    
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setPeriods(self, periods):
        self.periods = periods
    
    def setSize(self, sizeCells):
        self.sizeCells = sizeCells
    
    def setCells(self, cells):
        self.cells = cells
    
    def setAnalysis(self, analysis):
        self.analysis = analysis

    def setIndex(self, index):
        self.index = index
    
    def setResult(self, result):
        self.result = result
    