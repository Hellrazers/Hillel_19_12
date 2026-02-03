import unittest

def divide(x, y):
    return x / y

class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = divide(5, 0)

        with self.assertRaises(TypeError):
            result = divide(5, "1")

        self.assertEqual(result, 0, msg="Divide by zero failed")
        assert 1 != 1, "asserrt FAIL"
    # assert

if __name__ == '__main__':
    unittest.main()