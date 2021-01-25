import unittest,time
from main import *

class TestFunction(unittest.TestCase):

    currentResult = None # Holds last result object passed to run method

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_keygen_make(self):
        key = keygen_make('halo')
        self.assertEqual(key[0], '|h|a|l|o|')

    def test_keygen_hash(self):
        pass

    def test_encrypt(self):
        toBeEncrypt = encrypt('halo','1234')
        self.assertTrue(toBeEncrypt)
        self.assertIsNotNone(toBeEncrypt)
        self.assertIn('|',toBeEncrypt[0])

    def test_decrypt(self):
        toBeDecrypt = decrypt('|e|0|a|648|a|124|e|0|a|477|540|f|e|0|a|558|522|308|e|0|a|675|675|b|',
            '|36|57|57|55|65|76|77|85|26|57|45|47|37|06|35|85|96|45|26|66|27|07|27|75|','1234')
        self.assertIsNotNone(toBeDecrypt)
        self.assertEqual(toBeDecrypt,'halo')

    def test_isOnline(self):
        self.assertEqual(isOnline(), True)

    def test_isEmail(self):
        self.assertEqual(isEmail('toke.system@gmail.com'), True)
        self.assertEqual(isEmail('toke.systemgmail.com'), False)
        self.assertEqual(isEmail('toke.system@gmail'), False)

if __name__ == '__main__':
    test = unittest.main(verbosity=2,exit=False)
    print(test.result)
    time.sleep(15)