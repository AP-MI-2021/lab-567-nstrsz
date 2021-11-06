from Domain.cheltuiala import getData, getId, getNrApartament, getSuma, getTip, creeazaCheltuiala


def adunareValLaCheltuielileDintr_oData(valoareDeAdunat, data, lista):
    '''
    aduna o valoare la toate cheltuielile dintr-o data citita
    :param valoareDeAdunat: valoarea de adunat, float
    :param data: data citita, string
    :param lista: lista de cheltuieli
    :return: lista continand cheltuielile a caror valoare a fost modificata cat si cele nemodificate
    '''

    listaNoua = []
    for cheltuiala in lista:
        if data == getData(cheltuiala):
            cheltuialaModificata = creeazaCheltuiala(
                getId(cheltuiala),
                getNrApartament(cheltuiala),
                getSuma(cheltuiala) + valoareDeAdunat,
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaNoua.append(cheltuialaModificata)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua


def determinaCeaMaiMareIntretinere(lista):
    '''
    determina cea mai mare cheltuiala de tipul intretinere dintr-o lista
    :param lista: lista de cheltuieli
    :return: cea mai mare cheltuiala de tipul intretinere
    '''
    ok = True
    for cheltuiala in lista:
        if getTip(cheltuiala) == "intretinere":
            if ok == True:
                ceaMaiMareCheltuiala = cheltuiala
                ok = False
            elif getSuma(cheltuiala) > getSuma(ceaMaiMareCheltuiala):
                ceaMaiMareCheltuiala = cheltuiala
    return ceaMaiMareCheltuiala


def determinaCeaMaiMareCanal(lista):
    '''
    determina cea mai mare cheltuiala de tipul canal dintr-o lista
    :param lista: lista de cheltuieli
    :return: cea mai mare cheltuiala de tipul canal
    '''
    ok = True
    for cheltuiala in lista:
        if getTip(cheltuiala) == "canal":
            if ok == True:
                ceaMaiMareCheltuiala = cheltuiala
                ok = False
            elif getSuma(cheltuiala) > getSuma(ceaMaiMareCheltuiala):
                ceaMaiMareCheltuiala = cheltuiala
    return ceaMaiMareCheltuiala


def determinaCeaMaiMareAlteCheltuieli(lista):
    '''
    determina cea mai mare cheltuiala de tipul alte cheltuieli dintr-o lista
    :param lista: lista de cheltuieli
    :return: cea mai mare cheltuiala de tipul alte cheltuieli
    '''
    ok = True
    ceaMaiMareCheltuiala = lista[0]
    for cheltuiala in lista:
        if getTip(cheltuiala) == "alte cheltuieli":
            if ok == True:
                ceaMaiMareCheltuiala = cheltuiala
                ok = False
            elif getSuma(cheltuiala) > getSuma(ceaMaiMareCheltuiala):
                ceaMaiMareCheltuiala = cheltuiala
    return ceaMaiMareCheltuiala


