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
            self.last.next = new
            self.last = new
    
    def analize(self):
        temp = self.head
        response = 'Mortal'
        status = False
        while temp != None:
            if temp.next != None:
                if temp.dato.getPattern() == temp.next.dato.getPattern():
                    status = True
                    break
            if self.searchPattern(temp.dato.getPattern()) > 1:
                status = True
                response = 'Grave'
                break
            temp = temp.next

        return {'response': response, 'status': status}

    def analizeFirst(self):
        return self.head.dato.getPattern() == self.head.next.dato.getPattern()

    def searchPatternFirst(self):
        return self.searchPattern(self.head.dato.getPattern() ) > 1

    def searchPattern(self, pattern):
        temp = self.head
        count = 0
        while temp != None:
            if temp.dato.getPattern() == pattern:
                count += 1
            temp = temp.next
        return count