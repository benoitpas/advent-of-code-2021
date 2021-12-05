from day3 import part1
import day5
import unittest

class TestDay4(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(5, day5.part1("day5_input_test.txt"))

if __name__ == '__main__':
    unittest.main()