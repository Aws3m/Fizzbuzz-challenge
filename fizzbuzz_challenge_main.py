"""FizzBuzz
Write a program that prints the numbers from 1 to 100.
But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.
Please also include any test you deem necessary."""

def fizzbuzz(index):
    if (index % 3 == 0) and (index % 5 == 0):
        return "FizzBuzz"
    elif index % 3 == 0:
        return "Fizz"
    elif index % 5 == 0:
        return "Buzz"
    else:
        return index

def main():
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()