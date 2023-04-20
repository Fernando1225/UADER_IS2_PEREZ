import unittest

class Factorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.results = {}
        return cls._instance

    def factorial_calculate(self, num):
        if num in self.results:
            return self.results[num]
        if num == 0:
            result = 1
        else:
            result = num * self.factorial_calculate(num - 1)
        self.results[num] = result
        return result


class TestFactorialSingleton(unittest.TestCase):
    def test_singleton(self):
        factorial = Factorial()
        factorial2 = Factorial()
        self.assertIs(factorial, factorial2)

if __name__ == '__main__':
    unittest.main()


# factorial = Factorial()
# # Return 120
# print(factorial.factorial_calculate(5))
# # Reutrn 3628800
# print(factorial.factorial_calculate(10))

