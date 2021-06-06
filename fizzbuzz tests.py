import unittest
import fizzbuzz_challenge_main

class fizzbuzzChallenge(unittest.TestCase):

    def test_multiplesOfThree(self):
        for i in [3, 6, 9, 36]:
            assert fizzbuzz_challenge_main.fizzbuzz(i) == "Fizz", "expected Fizz"

    def test_multiplesOfFive(self):
        for i in [5, 10, 50, 95]:
            assert fizzbuzz_challenge_main.fizzbuzz(i) == "Buzz", "expected Buzz"

    def test_MultiplesOfThreeAndFive(self):
        for i in [15, 30, 45, 75]:
            assert fizzbuzz_challenge_main.fizzbuzz(i) == "FizzBuzz", "expected FizzBuzz"

    def test_regularNumbers(self):
        for i in [2, 4, 41, 88]:
            assert fizzbuzz_challenge_main.fizzbuzz(i) == i, "expected number"

if __name__ == '__main__':
    unittest.main()
