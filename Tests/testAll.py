from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala, testGetByNrApartament, testModificaCheltuiala
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testAdunareValLaCheltuielileDintr_Data, testDetCeleMaiMariCheltuieliPerTip, \
    testOrdonareDescDupaSuma, testSumeLunarePerApartament, testDoUndoDoRedo


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()
    testModificaCheltuiala()
    testAdunareValLaCheltuielileDintr_Data()
    testGetByNrApartament()
    testDetCeleMaiMariCheltuieliPerTip()
    testOrdonareDescDupaSuma()
    testSumeLunarePerApartament()
    testDoUndoDoRedo()