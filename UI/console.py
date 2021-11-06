from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Logic.functionalitati import adunareValLaCheltuielileDintr_oData, determinaCeaMaiMareIntretinere, \
    determinaCeaMaiMareCanal, determinaCeaMaiMareAlteCheltuieli


def printMenu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Adunarea unei valori la toate cheltuielile dintr-o data")
    print("5. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("a. Afiseaza cheltuielile")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    id = int(input("Dati id-ul: "))
    nrApartament = int(input("Dati numarul apartamentului: "))
    suma = float(input("Dati suma: "))
    data = input("Dati data: ")
    tipul = input("Dati tipul: ")
    return adaugaCheltuiala(id, nrApartament, suma, data, tipul, lista)


def uiStergeCheltuiala(lista):
    nrApartament= int(input("Dati numarul apartamentului: "))
    return stergeCheltuiala(nrApartament,lista)


def uiModificaCheltuiala(lista):
    id = int(input("Dati noul id: "))
    nrApartament = int(input("Dati numarul apartamentului: "))
    suma = float(input("Dati noua suma: "))
    data = input("Dati noua data: ")
    tipul = input("Dati noul tip: ")
    return modificaCheltuiala(id, nrApartament, suma, data, tipul,lista)


def uiAdunareValLaCheltuielileDintr_oData(lista):
    valoareDeAdunat = float(input("Dati valoarea de adunat: "))
    data = input("Dati data: ")
    return adunareValLaCheltuielileDintr_oData(valoareDeAdunat, data, lista)


def uiDeterminaCeleMaiMariCheltuieliPtFiecareTip(lista):
    print("Intretinere: ", toString(determinaCeaMaiMareIntretinere(lista)))
    print("Canal: ", toString(determinaCeaMaiMareCanal(lista)))
    print("Alte Cheltuieli: ", toString(determinaCeaMaiMareAlteCheltuieli(lista)))


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
        elif optiune == "4":
            lista = uiAdunareValLaCheltuielileDintr_oData(lista)
        elif optiune == "5":
            uiDeterminaCeleMaiMariCheltuieliPtFiecareTip(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")

