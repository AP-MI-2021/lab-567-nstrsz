from Domain.cheltuiala import getData, getId, getNrApartament, getSuma, getTip, creeazaCheltuiala


def adunareValLaCheltuielileDintr_oData(valoareDeAdunat, data, lista):
    '''
    aduna o valoare la toate cheltuielile dintr-o data citita
    :param valoareDeAdunat: valoarea de adunat, float
    :param data: data citita, string
    :param lista: lista de cheltuieli
    :return: lista continand cheltuielile a caror valoare a fost modificata cat si cele nemodificate
    '''
    if valoareDeAdunat < 0 :
        raise ValueError("Valoarea de adunat este negativa!")
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


def detCeleMaiMariCheltuieliPerTip(lista):
    '''
    creeaza un dictionar in care tipurile de cheltuieli sunt chei iar valorile sunt cea mai mare cheltuiala de tipul dat
    :param lista: lista de cheltuieli
    :return: un dictionar in care tipurile de cheltuieli sunt chei iar valorile sunt cea mai mare cheltuiala de tipul dat
    '''

    rezultat = {}
    for cheltuiala in lista:
        tip = getTip(cheltuiala)
        if tip in rezultat:
            if rezultat[tip] < getSuma(cheltuiala):
                rezultat[tip] = getSuma(cheltuiala)
        else:
            rezultat[tip] = getSuma(cheltuiala)
    return rezultat


def ordonareDescDupaSuma(lista):
    '''
    returneaza o lista ordonata descrescator dupa suma cheltuielilor
    :param lista: lista initiala de cheltuieli
    :return: lista ordonata descrescator dupa suma cheltuielilor
    '''

    return sorted(lista, key = getSuma, reverse=True)


def sumeLunarePerApartament(lista):
    '''

    :param lista:
    :return:
    '''

    apartamente = {}
    for cheltuiala in lista:
        nrApartament = getNrApartament(cheltuiala)
        if nrApartament in apartamente:
            dataImpartita=getData(cheltuiala).split('.')
            data = dataImpartita[1] + "." + dataImpartita[2]
            if data in apartamente[nrApartament]:
                apartamente[nrApartament][data] = apartamente[nrApartament][data] + getSuma(cheltuiala)
            else:
                apartamente[nrApartament][data] = getSuma(cheltuiala)
        else:
            apartamente[nrApartament] = {}
            dataImpartita = getData(cheltuiala).split('.')
            data = dataImpartita[1] + "." + dataImpartita[2]
            apartamente[nrApartament][data] = getSuma(cheltuiala)
    return apartamente
