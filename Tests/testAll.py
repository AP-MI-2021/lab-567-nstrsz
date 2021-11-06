from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testAdunareValLaCheltuielileDintr_Data, \
    testDeterminaCeleMaiMariCheltuieliPentruFiecareTip


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()
    testAdunareValLaCheltuielileDintr_Data()
    testDeterminaCeleMaiMariCheltuieliPentruFiecareTip()