from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()

    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 5, 400, "11.02.2021", "canal", lista)
    lista = adaugaCheltuiala(4, 23, 235, "11.02.2021", "alte cheltuieli", lista)
    lista = adaugaCheltuiala(5, 99, 550, "11.02.2021", "canal", lista)
    lista = adaugaCheltuiala(6, 19, 300, "11.02.2021", "alte cheltuieli", lista)


    runMenu(lista)

main()