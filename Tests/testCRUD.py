from Domain.cheltuiala import getId, getNrApartament, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNrApartament, stergeCheltuiala, modificaCheltuiala


def testAdaugaCheltuiala():
    redoList=[]
    undoList=[]
    lista=[]
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", lista, undoList, redoList)
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
    redoList = []
    undoList = []
    lista = []
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 235, "23.12.2020", "intretinere", lista, undoList, redoList)

    lista=stergeCheltuiala(343,lista, undoList, redoList)
    assert len(lista) == 1
    assert getByNrApartament(343, lista) is None

    try:
        lista= stergeCheltuiala(10, lista, undoList, redoList)
    except ValueError:
        assert len(lista) == 1
        assert getByNrApartament(18, lista) is not None
    except Exception:
        assert False



def testModificaCheltuiala():
    redoList = []
    undoList = []
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", [], undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 235, "23.12.2020", "intretinere", lista, undoList, redoList)

    lista = modificaCheltuiala(1,343,70,"9.08.2018", "intretinere", lista, undoList, redoList)

    cheltuialaUpdatata = getByNrApartament(343,lista)
    assert getId(cheltuialaUpdatata) == 1
    assert getNrApartament(cheltuialaUpdatata) == 343
    assert getSuma(cheltuialaUpdatata) == 70
    assert getData(cheltuialaUpdatata) == "9.08.2018"
    assert getTip(cheltuialaUpdatata) == "intretinere"

def testGetByNrApartament():
    redoList = []
    undoList = []
    lista = adaugaCheltuiala(1, 343, 235, "11.02.2011", "intretinere", [], undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 235, "23.12.2020", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 5, 40, "11.02.2021", "intretinere", lista, undoList, redoList)

    assert getByNrApartament(343,lista) == lista[0]
    assert getByNrApartament(5,lista) == lista[2]