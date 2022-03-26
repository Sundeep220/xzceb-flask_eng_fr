import unittest
from translator import englishTofrench,frenchToenglish

class Test_e2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishTofrench("Hello"),"Bonjour")

class Test_f2e(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToenglish("Bonjour"),"Hello")

unittest.main()
