from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Logic.functionalitati import adunareValLaCheltuielileDintr_oData, detCeleMaiMariCheltuieliPerTip, \
    ordonareDescDupaSuma, sumeLunarePerApartament, doUndo, doRedo


def printMenu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Adunarea unei valori la toate cheltuielile dintr-o data")
    print("5. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("6. Ordonarea cheltuielilor descrescător după sumă.")
    print("7. Afișarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afiseaza cheltuielile")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista,undoList,redoList):
    try:
        id = int(input("Dati id-ul: "))
        nrApartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma: "))
        data = input("Dati data: ")
        tipul = input("Dati tipul: ")

        rezultat = adaugaCheltuiala(id, nrApartament, suma, data, tipul, lista ,undoList,redoList)

        return rezultat


    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def uiStergeCheltuiala(lista,undoList,redoList):
    try:
        nrApartament= int(input("Dati numarul apartamentului: "))

        rezultat = stergeCheltuiala(nrApartament,lista,undoList,redoList)

        return rezultat


    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def uiModificaCheltuiala(lista,undoList,redoList):
    try:
        id = int(input("Dati noul id: "))
        nrApartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati noua suma: "))
        data = input("Dati noua data: ")
        tipul = input("Dati noul tip: ")

        rezultat = modificaCheltuiala(id, nrApartament, suma, data, tipul,lista,undoList,redoList)

        return rezultat


    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def uiAdunareValLaCheltuielileDintr_oData(lista,undoList,redoList):
    try:
        valoareDeAdunat = float(input("Dati valoarea de adunat: "))
        data = input("Dati data: ")

        rezultat = adunareValLaCheltuielileDintr_oData(valoareDeAdunat, data, lista,undoList,redoList)

        return rezultat


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
        print("Apartamentul {} are cheltuielile: ". format(nrApartament))
        for data in rezultat[nrApartament]:
            print ("* In luna {} in valoare de {}".format(data, rezultat[nrApartament][data]))


def runMenu(lista):
    undoList=[]
    redoList=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista,undoList,redoList)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista,undoList,redoList)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista,undoList,redoList)
        elif optiune == "4":
            lista = uiAdunareValLaCheltuielileDintr_oData(lista,undoList,redoList)
        elif optiune == "5":
            uiDetCeleMaiMariCheltuieliPerTip(lista)
        elif optiune == "6":
            uiOrdonareDescDupaSuma(lista)
        elif optiune == "7":
            uiSumeLunarePerApartament(lista)
        elif optiune == "u":
            lista = doUndo(lista,undoList,redoList)
        elif optiune == "r":
            lista = doRedo(lista,undoList,redoList)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")

