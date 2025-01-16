# Sieve of Eratosthenes

This project implements the Sieve of Eratosthenes algorithm in Python. The Sieve of Eratosthenes is an ancient and efficient algorithm for finding all prime numbers up to a given limit.

## Algorithm Description

The Sieve of Eratosthenes works by iteratively marking the multiples of each prime number as composite (not prime), starting from 2. The algorithm follows these steps:

1. Create a list of consecutive integers from 2 to n
2. Start with the smallest prime number (2)
3. Mark all its multiples as composite
4. Move to the next unmarked number and repeat step 3
5. Continue until reaching the square root of n

## Usage

```python
from sieve import sieve_of_eratosthenes

# Find all prime numbers up to 100
primes = sieve_of_eratosthenes(100)
print(primes)
```

## Running the Program

To run the program directly:

```bash
python sieve.py
```

## Time Complexity

The time complexity of the Sieve of Eratosthenes algorithm is O(n log log n), making it one of the most efficient ways to find all prime numbers up to a given limit.

## Space Complexity

The space complexity is O(n) as we need to create a boolean array of size n + 1 to mark numbers as prime or composite.

## License

This project is open source and available under the MIT License.