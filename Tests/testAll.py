from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala
from Tests.testDomain import testCheltuiala


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()