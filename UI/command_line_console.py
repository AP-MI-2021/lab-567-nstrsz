from Domain.cheltuiala import toString
from Logic.CRUD import stergeCheltuiala, modificaCheltuiala, adaugaCheltuiala


def help():
    print("Instructiuni: Pentru crearea unei cheltuieli trebuie citite id-ul (nr intreg) , numarul apt. (nr intreg) , suma (nr. cu zecimale) , data si tipul cheltuielii ")
    print("Comenzile trebuie apelate pe o linie ,separate prin ' ; ' iar campurile prin ' , '  ")
    print("Sa nu se foloseasca alti separatori!")
    print(" add- adauga in lista o cheltuiala noua, fiind necesare datele adevcate separate prin virgula")
    print(" delete- sterge o cheltuiala,introducandu-se cu virgula dupa si numarul cheltuielii,acesta trebuie sa existe")
    print(" modify- modifica parametrii unei cheltuieli in functie de numarul de apartament")
    print(" showall- afiseaza toate cheltuielile din lista ")
    print(" iesire- daca doriti sa iesiti din meniu")

def add (id, nrApartament, suma, data, tip, lista, undoList, redoList):
    lista = adaugaCheltuiala(id, nrApartament, suma, data, tip, lista, undoList, redoList)
    return lista

def delete(nrApartament, lista, undoList, redoList):
    lista = stergeCheltuiala(nrApartament, lista, undoList, redoList)
    return lista

def modify(id, nrApartament, suma, data, tip, lista, undoList, redoList):
    lista = modificaCheltuiala(id, nrApartament, suma, data, tip, lista, undoList, redoList)
    return lista

def showall(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def runNewMenu(lista):
    undoList=[]
    redoList=[]
    quit = False
    print("Pentru ajutor scrieti 'help' ")
    while not quit:
        optiune = input("Scrieti comanda/comenzile dorite:")
        optiuni = optiune.split(';')
        for comenzi in optiuni:
            sir = comenzi.split(',')
            if sir[0] == "help":
                help()
            elif sir[0] == "add":
                id = int(sir[1])
                nrApartament = int(sir[2])
                suma = float(sir[3])
                data = sir[4]
                tip = sir[5]
                lista = add(id, nrApartament, suma, data, tip, lista, undoList, redoList)
            elif sir[0] == "delete":
                nrApartament = int(sir[1])
                lista = delete(nrApartament, lista, undoList, redoList)
            elif sir[0] == "showall":
                showall(lista)
            elif sir[0] == "modify":
                id = int(sir[1])
                nrApartament = int(sir[2])
                suma = float(sir[3])
                data = sir[4]
                tip = sir[5]
                lista = modify(id, nrApartament, suma, data, tip, lista, undoList, redoList)
            elif sir[0] == "iesire":
                quit = True