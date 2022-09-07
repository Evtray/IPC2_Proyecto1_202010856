from os import startfile, system
import os
from time import sleep


class Analysis:
    def __init__(self, indexPatiente, pattern, cells, period, size):
        self.indexPatiente = indexPatiente
        self.pattern = pattern
        self.cells = cells
        self.period = period
        self.size = size

    def generateGraph(self, name):
        try:
            graphviz = "digraph G{"
            graphviz += '''
                tbl [
                    shape=plaintext
                    label=<
                        <table cellspacing='4'>
                '''
            z = 1
            for value in self.pattern:
                graphviz += "<tr>" if z == 1 else ""
                graphviz += f'<td cellpadding="10" bgcolor="{"black" if value == "1" else "white"}"> <font color="{"white" if value == "1" else "black"}">{value}</font> </td>'
                graphviz += "</tr>" if z == int(self.size) else ""
                z = 1 if z == int(self.size) else z + 1
            graphviz += "</table>>];"
            graphviz += "}"
            miArchivo = open('graphviz.dot', 'w')
            miArchivo.write(graphviz)
            miArchivo.close()
            system('cd ./graphs && mkdir ' + name)
            namedir = './graphs/'+ name +'/graphviz-no' + str(self.period) + '.png'
            system('dot -Tpng graphviz.dot -o ' + namedir)
            print("Generando dot...")
        except:
            print("")
    
    def printCells(self):
        sleep(1)
        count = 1
        print("Periodo: No. ", self.period)
        for value in self.pattern:
            value = "#" if value == "1" else "."
            print(f'{value} ', end=" ")
            if count == int(self.size):
                print()
                count = 1
            else:
                count += 1
        print("------------------------------------------------")

    def getIndexPatiente(self):
        return self.indexPatiente

    def getPattern(self):
        return self.pattern
    
    def getCells(self):
        return self.cells
    
    def getPeriod(self):
        return self.period
    
    def getSize(self):
        return self.size
    
    def setIndexPatiente(self, indexPatiente):
        self.indexPatiente = indexPatiente

    def setPattern(self, pattern):
        self.pattern = pattern
    
    def setCells(self, cells):
        self.cells = cells
    
    def setPeriod(self, period):
        self.period = period
    
    def setSize(self, size):
        self.size = size
