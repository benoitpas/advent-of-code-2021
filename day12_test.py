import unittest
import day12

class TestDay12(unittest.TestCase):
    def setUp(self):
        cnx = ["start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end"]
        self.cm = day12.cnx2map(cnx)

    def test_part1(self):
        self.assertEqual(10, day12.countPaths(self.cm, True))

    def test_part2(self):
        self.assertEqual(36, day12.countPaths(self.cm, False))

if __name__ == '__main__':
    unittest.main()
