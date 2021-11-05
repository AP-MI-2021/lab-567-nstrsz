from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", [])
    lista = adaugaCheltuiala(2, 18, 235, "23.12.2020", "intretinere", lista)
    runMenu(lista)

main()