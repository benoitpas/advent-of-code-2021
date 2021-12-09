import unittest
import day9

class TestDay9(unittest.TestCase):
    def setUp(self):
        r = day9.part12("day9_input_test.txt")
        self.part1 = r[0]
        self.part2 = r[1]

    def test_part1(self):
        self.assertEqual(15, self.part1)

    def test_part2(self):
        self.assertEqual(1134, self.part2)

if __name__ == '__main__':
    unittest.main()
