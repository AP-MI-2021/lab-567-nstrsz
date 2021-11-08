from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala, testGetByNrApartament
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testAdunareValLaCheltuielileDintr_Data, \
    testDeterminaCeleMaiMariCheltuieliPentruFiecareTip


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()
    testAdunareValLaCheltuielileDintr_Data()
    testDeterminaCeleMaiMariCheltuieliPentruFiecareTip()
    testGetByNrApartament()