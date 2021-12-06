import unittest
import day6

class TestDay6(unittest.TestCase):
    def setUp(self):
        day6_input_test = "3,4,3,1,2,"
        r = day6.part12(day6_input_test)
        self.part1 = r[0]
        self.part2 = r[1]

    def test_part1(self):
        self.assertEqual(5934, self.part1)

    def test_part2(self):
        self.assertEqual(26984457539, self.part2)

if __name__ == '__main__':
    unittest.main()
