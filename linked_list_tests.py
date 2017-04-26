import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_repr_01(self):
        self.assertEqual(repr(Pair(2, None)), 'Pair(2, None)')
    
    def test_empty_list_01(self):
        self.assertEqual(empty_list(), None)

    def test_add_01(self):
        self.assertEqual(add(None, 0, 5), Pair(5, None))

    def test_add_02(self):
        List = Pair(1, Pair(3, Pair(9, None)))
        self.assertEqual(add(List, 1, "hollup"), Pair(1, Pair("hollup", Pair(3, Pair(9, None)))))

    def test_add_03(self):
        with self.assertRaises(IndexError):
            List = Pair(10, Pair(2, Pair(19, None)))
            add(List, 20, 20)

    def test_length_01(self):
        self.assertEqual(length(None), 0)

    def test_length_02(self):
        self.assertEqual(length(Pair(2, Pair(10, Pair(9, None)))), 3)

    def test_get_01(self):
        with self.assertRaises(IndexError):
            get(Pair(1, None), 3)

    def test_get_02(self):
        self.assertEqual(get(Pair(2, Pair(18, Pair(36, None))), 1), 18)

    def test_set_01(self):
        with self.assertRaises(IndexError):
            set(Pair(1, None), 3, 'a')

    def test_set_02(self):
        self.assertEqual(set(Pair(8, Pair(2, Pair(6, None))), 2, 'abc'), Pair(8, Pair(2, Pair('abc', None))))

    def test_remove_01(self):
        with self.assertRaises(IndexError):
            remove(Pair(1, Pair(2, None)), 6)

    def test_remove_02(self):
        self.assertEqual(remove(Pair(3, Pair(5, Pair(2, None))), 1), (5, Pair(3, Pair(2, None))))

if __name__ == '__main__':
    unittest.main()
