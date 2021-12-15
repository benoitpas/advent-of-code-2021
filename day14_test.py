import unittest
import day14

class TestDay14(unittest.TestCase):
    def setUp(self):
        polymer = "NNCB"

        mapping = {
            "CH" : "B",
            "HH" : "N",
            "CB" : "H",
            "NH" : "C",
            "HB" : "C",
            "HC" : "B",
            "HN" : "C",
            "NN" : "C",
            "BH" : "H",
            "NC" : "B",
            "NB" : "B",
            "BN" : "B",
            "BB" : "N",
            "BC" : "B",
            "CC" : "N",
            "CN" : "C"}

        r = day14.part12(polymer, mapping)
        self.part1 = r[0]
        self.part2 = r[1]

    def test_one_fold(self):
        self.assertEqual(1588, self.part1)

    def test_two_one_folds(self):
        self.assertEqual(2188189693529, self.part2)

if __name__ == '__main__':
    unittest.main()
