import unittest
from stat_func import add
class ModeTest(unittest.TestCase):
    def setUp(self):
       
        print("Setup executed")
    def testc(self):
       
        self.assertEqual(add(9,9),18)
    def tearDown(self):
            
        print("tearDown executed")
if __name__=="__main__":
    unittest.main()
