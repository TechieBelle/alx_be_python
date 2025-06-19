import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Basic addition tests
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

        # Test with negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)

        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=7)
        self.assertAlmostEqual(self.calc.add(-1.5, 2.8), 1.3, places=7)

        # Test with large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

        # Test with very small numbers
        self.assertAlmostEqual(self.calc.add(0.0001, 0.0002), 0.0003, places=7)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Basic subtraction tests
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

        # Test with negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)

        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2, places=7)
        self.assertAlmostEqual(self.calc.subtract(-1.5, -2.8), 1.3, places=7)

        # Test with large numbers
        self.assertEqual(self.calc.subtract(3000000, 1000000), 2000000)

        # Test with very small numbers
        self.assertAlmostEqual(self.calc.subtract(0.0003, 0.0001), 0.0002, places=7)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Basic multiplication tests
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1, 7), 7)

        # Test with negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(5, -2), -10)

        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2.0), -3.0, places=7)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)

        # Test with large numbers
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)

        # Test with fractions
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25, places=7)

    def test_division(self):
        """Test the division method."""
        # Basic division tests
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(7, 1), 7)

        # Test with negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        self.assertEqual(self.calc.divide(6, -2), -3)

        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)
        self.assertAlmostEqual(self.calc.divide(-9.0, 3.0), -3.0, places=7)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333, places=7)

        # Test with fractions
        self.assertAlmostEqual(self.calc.divide(0.5, 0.25), 2.0, places=7)

        # Test with large numbers
        self.assertEqual(self.calc.divide(1000000, 1000), 1000)

    def test_division_by_zero(self):
        """Test division by zero raises appropriate exception or returns expected value."""
        # Test division by zero - this should raise a ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(-5, 0)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0, 0)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(3.14, 0.0)

    def test_edge_cases(self):
        """Test additional edge cases and boundary conditions."""
        # Test with very large numbers
        large_num = 10 ** 10
        self.assertEqual(self.calc.add(large_num, large_num), 2 * large_num)
        self.assertEqual(self.calc.subtract(large_num, large_num), 0)

        # Test with very small numbers (close to zero)
        small_num = 1e-10
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2 * small_num, places=15)

        # Test operations that result in zero
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.multiply(0, 999999), 0)
        self.assertEqual(self.calc.divide(0, 1), 0)

    def test_method_return_types(self):
        """Test that methods return the expected data types."""
        # All operations should return numeric types
        result = self.calc.add(1, 2)
        self.assertIsInstance(result, (int, float))

        result = self.calc.subtract(5, 3)
        self.assertIsInstance(result, (int, float))

        result = self.calc.multiply(2, 3)
        self.assertIsInstance(result, (int, float))

        result = self.calc.divide(6, 2)
        self.assertIsInstance(result, (int, float))

    def test_calculator_instance(self):
        """Test that the calculator instance is properly created."""
        self.assertIsInstance(self.calc, SimpleCalculator)

        # Test that we can create multiple instances
        calc2 = SimpleCalculator()
        self.assertIsInstance(calc2, SimpleCalculator)

        # Test that instances are independent
        self.assertIsNot(self.calc, calc2)


if __name__ == '__main__':
    # This allows the test to be run directly from the command line
    unittest.main(verbosity=2)