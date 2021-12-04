import day3
import unittest

class TestDay4(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(4512, day3,part1("day4_input_test.txt"))

if __name__ == '__main__':
    unittest.main()