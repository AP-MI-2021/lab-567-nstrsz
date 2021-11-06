from Domain.cheltuiala import getSuma
from Logic.CRUD import adaugaCheltuiala
from Logic.functionalitati import adunareValLaCheltuielileDintr_oData, determinaCeaMaiMareIntretinere, \
    determinaCeaMaiMareCanal, determinaCeaMaiMareAlteCheltuieli


def testAdunareValLaCheltuielileDintr_Data():
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 5, 40, "11.02.2021", "intretinere", lista)

    lista = adunareValLaCheltuielileDintr_oData(30,"11.02.2021",lista)

    assert getSuma(lista[0]) == 230
    assert getSuma(lista[1]) == 50
    assert getSuma(lista[2]) == 70


def testDeterminaCeleMaiMariCheltuieliPentruFiecareTip():
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista)
    lista = adaugaCheltuiala(3, 5, 400, "11.02.2021", "canal", lista)
    lista = adaugaCheltuiala(4, 23, 235, "11.02.2021", "alte cheltuieli", lista)
    lista = adaugaCheltuiala(5, 99, 550, "11.02.2021", "canal", lista)
    lista = adaugaCheltuiala(6, 19, 300, "11.02.2021", "alte cheltuieli", lista)

    assert determinaCeaMaiMareIntretinere(lista) == lista[0]
    assert determinaCeaMaiMareCanal(lista) == lista[4]
    assert determinaCeaMaiMareAlteCheltuieli(lista) == lista[5]