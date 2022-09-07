from time import sleep
from lists.ListPatient import ListPatient

listPatients = ListPatient()

def main():
    global listPatients
    print("Hello World!")
    input("Press Enter to continue...")

    flag = True
    while flag:
        printTitle("Menu Principal")
        print("1. Añadir Pacientes")
        print("2. Analizar")
        print("3. Analizar")
        print("4. Salir")
        printTitle("")
        option = input("Seleccione una opción: ")
        if option == "1":
            menuPatiente()
        elif option == "2":
            menuAnalizar()
        elif option == "3":
            listPatients.generateXml()
        elif option == "4":
            flag = False
        else:
            printNoValidate()

def printTitle(title):
    print("------------------------------------------------")
    print(f'{title}')

def printNoValidate():
    printTitle("Opción no válida")
    input("Press Enter to continue...")

def menuPatiente():
    global listPatients
    flag = True
    while flag:
        printTitle('Menu Añadir pacientes')
        print("1. Añadir pacientes")
        print("2. Regresar")
        option = input("Seleccione una opción: ")

        if option == "1":
            printTitle('Añadir pacientes')

            route = input("Ingrese la ruta del archivo: ")
            response = listPatients.readFile(route)
            sleep(2)
            if response:
                printTitle("Pacientes añadidos correctamente")
            else:
                printTitle("Error al añadir pacientes")

        elif option == "2":
            flag = False

        else:
            printNoValidate()

def menuAnalizar():
    global listPatients
    flag = True
    while flag:
        printTitle('Menu Analizar')
        print("1. Analizar paciente")
        print("2. Analizar todos los pacientes")
        print("3. Regresar")
        option = input("Seleccione una opción: ")

        if option == "1":
            printTitle('Analizar paciente')
            name = input("Ingrese el nombre del paciente: ")
            printTitle('Analizando...')
            listPatients.analyzePatient(name)

        elif option == "2":
            printTitle('Analizando...')
            listPatients.analyzeAll()

        elif option == "3":
            flag = False

        else:
            printNoValidate()

if __name__ == "__main__":
    main()