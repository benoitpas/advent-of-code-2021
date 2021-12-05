import unittest
import day4

class TestDay4(unittest.TestCase):
    def setUp(self):
        r = day4.part12("day4_input_test.txt")
        self.part1 = r[0]
        self.part2 = r[1]

    def test_part1(self):
        self.assertEqual(4512, self.part1)

    def test_part2(self):
        self.assertEqual(1924, self.part2)

if __name__ == '__main__':
    unittest.main()
