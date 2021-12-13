import unittest
import day13

class TestDay13(unittest.TestCase):
    def setUp(self):
        lines = [
            "6,10",
            "0,14",
            "9,10",
            "0,3",
            "10,4",
            "4,11",
            "6,0",
            "6,12",
            "4,1",
            "0,13",
            "10,12",
            "3,4",
            "3,0",
            "8,4",
            "1,10",
            "2,14",
            "8,10",
            "9,0"]
        
        points = [day13.to_point(p) for p in lines]
        self.points2 = day13.foldy(points, 7)
        self.points3 = day13.foldx(self.points2, 5)

        
    def test_one_fold(self):
        self.assertEqual(17, len(self.points2))

    def test_two_one_folds(self):
        self.assertEqual(16, len(self.points3))

if __name__ == '__main__':
    unittest.main()
