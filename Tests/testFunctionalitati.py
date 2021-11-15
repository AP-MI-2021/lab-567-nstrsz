from Domain.cheltuiala import getSuma, getId, getNrApartament
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.functionalitati import adunareValLaCheltuielileDintr_oData, detCeleMaiMariCheltuieliPerTip, \
    ordonareDescDupaSuma, sumeLunarePerApartament, doUndo, doRedo


def testAdunareValLaCheltuielileDintr_Data():
    undoList=[]
    redoList=[]
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 5, 40, "11.02.2021", "intretinere", lista, undoList, redoList)

    lista = adunareValLaCheltuielileDintr_oData(30,"11.02.2021",lista, undoList, redoList)

    assert getSuma(lista[0]) == 230
    assert getSuma(lista[1]) == 50
    assert getSuma(lista[2]) == 70


def testDetCeleMaiMariCheltuieliPerTip():
    undoList = []
    redoList = []
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 5, 400, "11.02.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(4, 23, 235, "11.02.2021", "alte cheltuieli", lista, undoList, redoList)
    lista = adaugaCheltuiala(5, 99, 550, "11.02.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(6, 19, 300, "11.02.2021", "alte cheltuieli", lista, undoList, redoList)

    rezultat = detCeleMaiMariCheltuieliPerTip(lista)

    len(rezultat) == 3
    assert rezultat["intretinere"] == 200
    assert rezultat["canal"] == 550
    assert rezultat["alte cheltuieli"] == 300

def testOrdonareDescDupaSuma():
    undoList = []
    redoList = []
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 5, 400, "11.02.2021", "canal", lista, undoList, redoList)

    rezultat = ordonareDescDupaSuma(lista)

    assert getId(rezultat[0]) == 3
    assert getId(rezultat[1]) == 1
    assert getId(rezultat[2]) == 2

def testSumeLunarePerApartament():
    undoList = []
    redoList = []
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 343, 400, "11.03.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(4, 343, 235, "11.02.2021", "alte cheltuieli", lista, undoList, redoList)

    rezultat = sumeLunarePerApartament(lista)

    assert len(rezultat[343]) == 2
    assert len(rezultat[18]) == 1
    assert rezultat[343]['02.2021'] == 435
    assert rezultat[18]['06.2021'] == 50
    assert rezultat[343]['03.2021'] == 400


def testDoUndoDoRedo():
    undoList=[]
    redoList=[]
    lista = []
    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 5, 400, "11.03.2021", "canal", lista, undoList, redoList)


    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 2
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3,lista) is None

    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 1
    assert getId(lista[0]) == 1
    assert getById(2, lista) is None
    assert getById(3, lista) is None

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById(1,lista) is None
    assert getById(2, lista) is None
    assert getById(3, lista) is None

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    #nu s-a schimbat nimic deoarece lista de undo era goala
    assert len(lista) == 0
    assert getById(1,lista) is None
    assert getById(2, lista) is None
    assert getById(3, lista) is None

    lista = adaugaCheltuiala(1, 343, 200, "11.02.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 18, 50, "16.06.2021", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 5, 400, "11.03.2021", "canal", lista, undoList, redoList)

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getId(lista[2]) == 3
    #nu s-a intamplat nimic deoarece lista redo era goala

    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 2
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3,lista) is None

    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 1
    assert getId(lista[0]) == 1
    assert getById(2, lista) is None
    assert getById(3, lista) is None

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3, lista) is None

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getId(lista[2]) == 3

    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 2
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3,lista) is None

    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 1
    assert getId(lista[0]) == 1
    assert getById(2, lista) is None
    assert getById(3, lista) is None

    lista = adaugaCheltuiala(4, 69, 400, "11.03.2021", "alte cheltuieli", lista, undoList, redoList)

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 4
    assert getById(3, lista) is None
    #nu face nimic deoarece lista redo era goala

    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 1
    assert getId(lista[0]) == 1
    assert getById(2, lista) is None
    assert getById(3, lista) is None
    assert getById(4, lista) is None

    if len(undoList) > 0:
        lista = doUndo(lista,undoList,redoList)
    assert len(lista) == 0
    assert getById(1, lista) is None
    assert getById(2, lista) is None
    assert getById(3, lista) is None
    assert getById(4, lista) is None

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getId(lista[0]) == 1
    assert getById(4, lista) is None
    assert getById(3, lista) is None

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 4
    assert getById(3, lista) is None

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 4
    assert getById(3, lista) is None
    #nu s-a intamplat nimic deoarece lista redo era goala



