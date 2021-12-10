import unittest
import day10

class TestDay10(unittest.TestCase):
    def setUp(self):
        r = day10.part12("day10_input_test.txt")
        self.part1 = r[0]
        self.part2 = r[1]

    def test_part1(self):
        self.assertEqual(26397, self.part1)

    def test_part2(self):
        self.assertEqual(288957, self.part2)

if __name__ == '__main__':
    unittest.main()
