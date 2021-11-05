from Domain.cheltuiala import creeazaCheltuiala, getId, getNrApartament, getSuma, getData, getTip


def testCheltuiala():
    cheltuiala = creeazaCheltuiala(1, 343, 235, "11.02.2011", "intretinere")
    assert getId(cheltuiala) == 1
    assert getNrApartament(cheltuiala) == 343
    assert getSuma(cheltuiala) == 235
    assert getData(cheltuiala) == "11.02.2011"
    assert getTip(cheltuiala) == "intretinere"