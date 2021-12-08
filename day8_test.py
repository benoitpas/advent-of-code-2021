import unittest
import day8

class TestDay4(unittest.TestCase):

    def test_part2(self):
        self.assertEqual(936117, day8.part2("day8_input_test.txt"))

if __name__ == '__main__':
    unittest.main()
