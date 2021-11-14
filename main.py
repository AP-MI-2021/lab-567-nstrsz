from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala
from Tests.testAll import runAllTests
from UI.command_line_console import runNewMenu
from UI.console import runMenu

def meniuri():
    print("1. Meniu standard")
    print("2. Meniu command line")
    print("x. Exit")



def main():
    runAllTests()

    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 343, 400, "11.03.2021", "canal", lista)
    lista = adaugaCheltuiala(4, 343, 235, "11.02.2021", "alte cheltuieli", lista)

    while True:
        meniuri()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runNewMenu(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")



main()