import unittest
import calculator as calc

class calculatorTestCases(unittest.TestCase):
    def testaddition(self):
        self.assertEqual(calc.addition(3,4), 7)
        self.assertEqual(calc.addition(-3,3), 0)
        self.assertEqual(calc.addition(0,4), 4)
    
    def testsubtraction(self):
        self.assertEqual(calc.subtraction(0,1), -1)
        self.assertEqual(calc.subtraction(-1,1), -2)
        self.assertEqual(calc.subtraction(-2,-2), 0)
        self.assertEqual(calc.subtraction(5,3), 2)

    def testmultiplication(self):
        self.assertEqual(calc.multiplication(0, 5), 0)
        self.assertEqual(calc.multiplication(3, 4), 12)
        self.assertEqual(calc.multiplication(-1, 2), -2)
        self.assertEqual(calc.multiplication(-4, -2), 8)

    def testdivision(self):
        self.assertEqual(calc.division(0, 3), 0)
        self.assertEqual(calc.division(12, 3), 4)
        # the only case that I feel that I need to explain:
        # this case ensures that a divide by zero exception
        # is thrown upon doing 5 / 0
        with self.assertRaises(ZeroDivisionError):
            calc.division(5, 0)


if __name__ == "__main__":
    unittest.main()
