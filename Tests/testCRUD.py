from Domain.cheltuiala import getId, getNrApartament, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNrApartament, stergeCheltuiala, modificaCheltuiala


def testAdaugaCheltuiala():
    lista=[]
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", lista)
    assert len(lista) == 1
    assert getId(getByNrApartament(343,lista)) == 1
    assert getNrApartament(getByNrApartament(343,lista)) == 343
    assert getSuma(getByNrApartament(343,lista)) == 235
    assert getData(getByNrApartament(343,lista)) == "11.02.2011"
    assert getTip(getByNrApartament(343,lista)) == "intretinere"

    # assert getId(list[0]) == 1
    # assert getNrApartament(list[0]) == 343
    # assert getSuma(list[0]) == 235
    # assert getData(list[0]) == "11.02.2011"
    # assert getTip(list[0]) == "intretinere"

def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 235, "23.12.2020", "intretinere", lista)

    lista=stergeCheltuiala(343,lista)
    assert len(lista) == 1
    assert getByNrApartament(343, lista) is None

    lista= stergeCheltuiala(10, lista)
    assert len(lista) == 1
    assert getByNrApartament(18, lista) is not None

def testModificaCheltuiala():
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", [])
    lista = adaugaCheltuiala(2, 18, 235, "23.12.2020", "intretinere", lista)

    lista = modificaCheltuiala(1,343,70,"9.08.2018", "intretinere", lista)

    cheltuialaUpdatata = getByNrApartament(343,list)
    assert getId(cheltuialaUpdatata) == 1
    assert getNrApartament(cheltuialaUpdatata) == 343
    assert getSuma(cheltuialaUpdatata) == 70
    assert getData(cheltuialaUpdatata) == "9.08.2018"
    assert getTip(cheltuialaUpdatata) == "intretinere"

def testGetByNrApartament():
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", [])
    lista = adaugaCheltuiala(2, 18, 235, "23.12.2020", "intretinere", lista)
    lista = adaugaCheltuiala(3, 5, 40, "11.02.2021", "intretinere", lista)

    assert getByNrApartament(343,lista) == lista[0]
    assert getByNrApartament(5,lista) == lista[2]