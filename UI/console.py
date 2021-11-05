from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala


def printMenu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("a. Afiseaza cheltuielile")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    id = input("Dati id-ul: ")
    nrApartament = input("Dati numarul apartamentului: ")
    suma = input("Dati suma: ")
    data = input("Dati data: ")
    tipul = input("Dati tipul: ")
    return adaugaCheltuiala(id, nrApartament, suma, data, tipul, lista)


def uiStergeCheltuiala(lista):
    nrApartament= input("Dati numarul apartamentului: ")
    return stergeCheltuiala(nrApartament,lista)


def uiModificaCheltuiala(lista):
    id = input("Dati noul id: ")
    nrApartament = input("Dati numarul apartamentului: ")
    suma = input("Dati noua suma: ")
    data = input("Dati noua data: ")
    tipul = input("Dati noul tip: ")
    return modificaCheltuiala(id, nrApartament, suma, data, tipul,lista)


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")

