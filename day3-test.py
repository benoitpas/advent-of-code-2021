import day3
import unittest

class TestDay3dId(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(198, day3.part1(day3.numbersTest))

    def test_part2(self):
        self.assertEqual(230, day3.part2(day3.numbersTest))

if __name__ == '__main__':
    unittest.main()