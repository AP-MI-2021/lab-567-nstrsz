from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Logic.functionalitati import adunareValLaCheltuielileDintr_oData, detCeleMaiMariCheltuieliPerTip, \
    ordonareDescDupaSuma, sumeLunarePerApartament


def printMenu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Adunarea unei valori la toate cheltuielile dintr-o data")
    print("5. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("6. Ordonarea cheltuielilor descrescător după sumă.")
    print("7. Afișarea sumelor lunare pentru fiecare apartament.")
    print("a. Afiseaza cheltuielile")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    try:
        id = int(input("Dati id-ul: "))
        nrApartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma: "))
        data = input("Dati data: ")
        tipul = input("Dati tipul: ")
        return adaugaCheltuiala(id, nrApartament, suma, data, tipul, lista)
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def uiStergeCheltuiala(lista):
    try:
        nrApartament= int(input("Dati numarul apartamentului: "))
        return stergeCheltuiala(nrApartament,lista)
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def uiModificaCheltuiala(lista):
    try:
        id = int(input("Dati noul id: "))
        nrApartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati noua suma: "))
        data = input("Dati noua data: ")
        tipul = input("Dati noul tip: ")
        return modificaCheltuiala(id, nrApartament, suma, data, tipul,lista)
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def uiAdunareValLaCheltuielileDintr_oData(lista):
    try:
        valoareDeAdunat = float(input("Dati valoarea de adunat: "))
        data = input("Dati data: ")
        return adunareValLaCheltuielileDintr_oData(valoareDeAdunat, data, lista)
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista



def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiDetCeleMaiMariCheltuieliPerTip(lista):
    rezultat = detCeleMaiMariCheltuieliPerTip(lista)
    for tip in rezultat:
        print("Tipul: {} are cheltuiala cea mai mare {}".format(tip, rezultat[tip]))


def uiOrdonareDescDupaSuma(lista):
    rezultat = ordonareDescDupaSuma(lista)

    showAll(rezultat)


def uiSumeLunarePerApartament(lista):
    rezultat = sumeLunarePerApartament(lista)
    for nrApartament in rezultat:
        for data in rezultat[nrApartament]:
            print ("Apartamentul {} are cheltuielile in luna {} in valoare de {}".format(nrApartament, data, rezultat[nrApartament][data]))


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
            uiDetCeleMaiMariCheltuieliPerTip(lista)
        elif optiune == "6":
            uiOrdonareDescDupaSuma(lista)
        elif optiune == "7":
            uiSumeLunarePerApartament(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")

