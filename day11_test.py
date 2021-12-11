import unittest
import day11

class TestDay11(unittest.TestCase):
    def setUp(self):
        self.s1 = day11.to_state(("11111", "19991", "19191", "19991", "11111"))
        self.s2 = day11.to_state(("34543", "40004", "50005", "40004", "34543"))
        self.s3 = day11.to_state(("45654", "51115", "61116", "51115", "45654"))
        r = day11.part12("day11_input_test.txt")
        self.part1 = r[0]
        self.part2 = r[1]

    def test_neighbours_simple(self):
        n = day11.neighbours(2,3,10)
        self.assertEqual(n, [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)])

    def test_neighbours_top(self):
        n = day11.neighbours(2,0,10)
        self.assertEqual(n, [(1, 0), (1, 1), (2, 1), (3, 0), (3, 1)])


    def test_next1(self):
        state = self.s1.copy()
        n = day11.next(state)
        self.assertEqual(n, 9)
        self.assertEqual(state, self.s2)

    def test_next2(self):
        state = self.s2.copy()
        n = day11.next(state)
        self.assertEqual(n, 0)
        self.assertEqual(state, self.s3)

    def test_part1(self):
        self.assertEqual(1656, self.part1)

    def test_part2(self):
        self.assertEqual(195, self.part2)

if __name__ == '__main__':
    unittest.main()
