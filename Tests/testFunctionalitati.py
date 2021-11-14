from Domain.cheltuiala import getSuma, getId, getNrApartament
from Logic.CRUD import adaugaCheltuiala
from Logic.functionalitati import adunareValLaCheltuielileDintr_oData, detCeleMaiMariCheltuieliPerTip, \
    ordonareDescDupaSuma, sumeLunarePerApartament


def testAdunareValLaCheltuielileDintr_Data():
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 5, 40, "11.02.2021", "intretinere", lista)

    lista = adunareValLaCheltuielileDintr_oData(30,"11.02.2021",lista)

    assert getSuma(lista[0]) == 230
    assert getSuma(lista[1]) == 50
    assert getSuma(lista[2]) == 70


def testDetCeleMaiMariCheltuieliPerTip():
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 5, 400, "11.02.2021", "canal", lista)
    lista = adaugaCheltuiala(4, 23, 235, "11.02.2021", "alte cheltuieli", lista)
    lista = adaugaCheltuiala(5, 99, 550, "11.02.2021", "canal", lista)
    lista = adaugaCheltuiala(6, 19, 300, "11.02.2021", "alte cheltuieli", lista)

    rezultat = detCeleMaiMariCheltuieliPerTip(lista)

    len(rezultat) == 3
    assert rezultat["intretinere"] == 200
    assert rezultat["canal"] == 550
    assert rezultat["alte cheltuieli"] == 300

def testOrdonareDescDupaSuma():
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 5, 400, "11.02.2021", "canal", lista)

    rezultat = ordonareDescDupaSuma(lista)

    assert getId(rezultat[0]) == 3
    assert getId(rezultat[1]) == 1
    assert getId(rezultat[2]) == 2

def testSumeLunarePerApartament():
 '''   lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 343, 400, "11.03.2021", "canal", lista)
    lista = adaugaCheltuiala(4, 343, 235, "11.02.2021", "alte cheltuieli", lista)

    rezultat = sumeLunarePerApartament(lista)

    assert len(rezultat[0]) == 2
    assert len(rezultat[1]) == 1
'''