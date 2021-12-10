import unittest
import day10

class TestDay10(unittest.TestCase):
    def setUp(self):
        r = day10.part1("day10_input_test.txt")
        self.part1 = r

    def test_part1(self):
        self.assertEqual(26397, self.part1)

if __name__ == '__main__':
    unittest.main()
