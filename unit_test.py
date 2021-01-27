import unittest,time
from main import *

os.system('mode 85,107')
print(f'''
          
                         ████████  ██████  ██   ██ ███████   
                            ██    ██    ██ ██  ██  ██       
                            ██    ██    ██ █████   █████   
                            ██    ██    ██ ██  ██  ██      
                            ██     ██████  ██   ██ ███████ 
                         Two   Original   Key   Encryption 
''')
print("=".center(85,"=")) ;print(" BEFORE BUILD CHECK ".center(85,"=")) ;print("=".center(85,"=")) ;print("\n")

class TestFunction(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rand_sleep(self):
        randSleep = rand_sleep(0,5)
        self.assertFalse(randSleep)
        self.assertIsNone(randSleep)

    def test_isExpired(self):
        exp = isExpired('2021-01-25')
        self.assertTrue(exp)
        self.assertIsNotNone(exp)
        self.assertEqual(exp, True)

    def test_check_regist(self):
        license = check_regist('julians1234','651-451-651-551-151-451-551-151-651-851-601-212-322-412-112-302-612-122-551-651-751-851')
        self.assertTrue(license)
        self.assertIsNotNone(license)
        self.assertEqual(license, 'expired')

    @unittest.skip("Write License File")
    def test_write_license(self):
        pass

    @unittest.skip("Status License Validation")
    def test_status_license(self):
        pass

    @unittest.skip("Open License File")
    def test_def_open_license(self):
        pass

    @unittest.skip("Check License Skipping")
    def test_def_check_license(self):
        pass

    @unittest.skip("Keygen Maker")
    def test_keygen_make(self):
        key = keygen_make('halo')
        self.assertEqual(key[0], '|h|a|l|o|')

    @unittest.skip("Keygen Hasher")
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
    test = unittest.main(verbosity=3,exit=False)
    print('RESULT : ', test.result)
    time.sleep(15)