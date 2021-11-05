from Domain.cheltuiala import creeazaCheltuiala, getNrApartament


def adaugaCheltuiala(id, nrApartament, suma, data, tip, lista):
    '''
    adauga o cheltuiala intr-o lista
    :param id: int
    :param nrApartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista cheltuieli
    :return: o lista continand atat cheltuielile vechi cat si noua cheltuiala
    '''
    cheltuiala = creeazaCheltuiala(id,nrApartament, suma, data, tip)
    return lista + [cheltuiala]

def getByNrApartament(nrApartament, lista):
    '''
    gaseste o cheltuiala cu nr de apartament dat intr-o lista
    :param nrApartament:int
    :param lista: lista de cheltuieli
    :return: cheltuiala cu id-ul dat din lista sau None, daca aceasta nu exista
    '''

    for cheltuiala in lista:
        if getNrApartament(cheltuiala) == nrApartament:
            return cheltuiala
    return None

def stergeCheltuiala(nrApartament,lista):
    '''
    sterge o cheltuiala dupa nrAp dintr-o lista
    :param nrApartament: nrAp al cheltuielii de sters, int
    :param lista: lista de cheltuieli
    :return: o lista continand cheltuielile cu nr ap diferit de nrApartament
    '''
    return [cheltuiala for cheltuiala in lista if getNrApartament(cheltuiala) != nrApartament]

def modificaCheltuiala(id, nrApartament, suma, data, tip, lista):
    '''
    modifica o cheltuiala intr-o lista
    :param id: int
    :param nrApartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista cheltuieli
    :return: o lista continand atat cheltuielile vechi cat si cea modificata
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getNrApartament(cheltuiala) == nrApartament:
            cheltuialaNoua = creeazaCheltuiala(id, nrApartament, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
