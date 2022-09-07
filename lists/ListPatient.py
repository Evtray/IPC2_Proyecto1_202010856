from time import sleep
import xml.etree.ElementTree as ET
from lists.ListCell import ListCell

from lists.Nodo import Nodo
from models.Cell import Cell
from models.Patient import Patient

class ListPatient:
    def __init__(self):
        self.head = None
        self.last = None
        self.index = 1
    
    def insert(self, patient):
        new = Nodo(patient) 

        if self.head == None:
            self.head = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
        self.index += 1


    def readFile(self, path):
        try:
            print("Leyendo archivo...")
            tree = ET.parse(path)
            root = tree.getroot()

            for nodo in root.findall('paciente'):
                nodoPatient = nodo.find('datospersonales')
                listCell = ListCell()
                for nodoCell in nodo.find('rejilla'):
                    attributes = nodoCell.attrib
                    cell = Cell(int(attributes['f']), int(attributes['c']))
                    listCell.insert(cell)
                
                patient = Patient(nodoPatient.find('nombre').text, int(nodoPatient.find('edad').text), int(nodo.find('periodos').text), int(nodo.find('m').text), listCell, self.index)
                self.insert(patient)
            return True
        except:
            return False

    def analyzePatient(self, name):
        sleep(2)
        patient = self.search(name)
        if patient != None:
            patient.analyze()
        else:
            print("Paciente no encontrado")
    
    def analyzeAll(self):
        sleep(2)
        temp = self.head
        while temp != None:
            temp.dato.analyze()
            temp = temp.next

    def search(self, name):
        temp = self.head
        while temp != None:
            if temp.dato.name == name:
                return temp.dato
            temp = temp.next
        return None
    
    def generateXml():
        print("Generando XML...")
        sleep(2)
        print("XML generado correctamente")