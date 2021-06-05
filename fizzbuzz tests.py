import unittest
import fizzbuzz_challenge_main

class fizzbuzzChallenge(unittest.TestCase):

    def test_multiplesOfThree(self):
        for i in [3, 6, 9, 36]:
            #self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(i), "Fizz", "expected Fizz, got something else")
            assert fizzbuzz_challenge_main.fizzbuzz(i) == "Fizz"

    def test_multiplesOfFive(self):
        for i in [5, 10, 50, 95]:
            #self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(i), "Buzz", "expected Buzz, got something else")
            assert fizzbuzz_challenge_main.fizzbuzz(i) == "Buzz"

    def test_MultiplesOfThreeAndFive(self):
        for i in [15, 30, 45, 75]:
            #self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(i), "FizzBuzz", "expected FizzBuzz, got something else")
            assert fizzbuzz_challenge_main.fizzbuzz(i) == "FizzBuzz"

    def test_regularNumbers(self):
        for i in [2, 4, 41, 88]:
            #self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(i), i, "expected numbers, got NaN")
            assert fizzbuzz_challenge_main.fizzbuzz(i) == i

if __name__ == '__main__':
    unittest.main()
