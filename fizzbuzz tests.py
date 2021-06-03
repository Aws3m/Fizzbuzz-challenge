import unittest
import fizzbuzz_challenge_main

class fizzbuzzChallenge(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(3), "Fizz", "expected Fizz, got something else")
        self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(5), "Buzz", "expected Buzz, got something else")
        self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(15), "FizzBuzz", "expected FizzBuzz, got something else")
        self.assertEqual(fizzbuzz_challenge_main.fizzbuzz(16), 16, "expected 16, got NaN")
if __name__ == '__main__':
    unittest.main()
