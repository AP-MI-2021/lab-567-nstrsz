def creeazaCheltuiala(id, nrApartament, suma, data, tip):
    '''
    creeaza o cheltuiala
    :param id: int
    :param nrApartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :return:  un dictionar ce retine o cheltuiala
    '''
    return {
        'id': id,
        'nrApartament': nrApartament,
        'suma': suma,
        'data': data,
        'tip': tip
    }


def getId(cheltuiala):
    '''
    ia id-ul cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: id-ul cheltuielii
    '''
    return cheltuiala['id']


def getNrApartament(cheltuiala):
    '''
    ia numarul de apartament al cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: numarul de apartament al cheltuielii
    '''
    return cheltuiala['nrApartament']


def getSuma(cheltuiala):
    '''
    ia suma cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: suma cheltuielii
    '''
    return cheltuiala['suma']


def getData(cheltuiala):
    '''
        ia data cheltuielii
        :param cheltuiala: dictionar de tipul cheltuiala
        :return: data cheltuielii
        '''
    return cheltuiala['data']

def getTip(cheltuiala):
    '''
        ia tipul cheltuielii
        :param cheltuiala: dictionar de tipul cheltuiala
        :return: tipul cheltuielii
        '''
    return cheltuiala['tip']

def toString(cheltuiala):
    return "id: {}, nrApartament: {}, suma: {}, data: {}, tip: {}".format(
        getId(cheltuiala),
        getNrApartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )