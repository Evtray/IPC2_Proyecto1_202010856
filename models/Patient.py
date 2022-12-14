from lists.ListAnalysis import ListAnalysis
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
    
    def analyze(self, periods = 0):
        print('Paciente: ', self.getName())
        print('Edad: ', self.getAge())
        print('Periodos: ', self.getPeriods())
        print("------------------------------------------------")

        defPeriod = int(periods) if int(periods) > 1 else self.periods

        listAnalysis = ListAnalysis()
        temporal = self.cells
        for i in range(1, defPeriod + 1):
            response = temporal.analize(self.size)
            temporal = response['cells']
            analysis = Analysis(self.index, response['pattern'], response['cells'], i, self.size)
            analysis.printCells()
            listAnalysis.insert(analysis)
            analysis.generateGraph(self.name)
        print(f'{1} patron despues del primero repetido')
        if listAnalysis.analizeFirst():
            self.setResult('Mortal - Encontrado en patron inicial')

        if listAnalysis.searchPatternFirst():
            self.setResult('Grave - Primer patron repetido en x > 1')
        
        analize = listAnalysis.analize()
        if analize['status']:
            self.setResult(f'{analize["response"]} - Patron x > 1 repetido')	
        else:
            self.setResult('Leve')

        print('Resultado: ', self.getResult())        

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getPeriods(self):
        return self.periods
    
    def getSize(self):
        return self.size
    
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
    
    def setSize(self, size):
        self.size = size
    
    def setCells(self, cells):
        self.cells = cells
    
    def setAnalysis(self, analysis):
        self.analysis = analysis

    def setIndex(self, index):
        self.index = index
    
    def setResult(self, result):
        self.result = result
    