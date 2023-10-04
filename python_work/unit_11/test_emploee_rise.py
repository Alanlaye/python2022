import unittest
from emploee import Emploee

class TestEmploee(unittest.TestCase):
    def setUp(self):
        self.emploee = Emploee('aa','bb')

    def test_give_defaullt_raise(self):
        self.emploee.give_raise()
        self.assertEqual(self.emploee.rise,5000)

    def test_give_custom_raise(self):
        self.emploee.give_raise(7000)
        self.assertEqual(self.emploee.rise,7000)

unittest.main()
#通过测试了，但是为什么会多打印一条。5000
#5000
#7000
#.5000
#.
