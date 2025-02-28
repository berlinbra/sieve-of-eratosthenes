def sieve_of_eratosthenes(n):
    """
    Implements the Sieve of Eratosthenes algorithm to find all prime numbers up to n.
    
    Args:
        n (int): Upper limit for finding prime numbers
    
    Returns:
        list: A list of prime numbers up to n
    """
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # Create the list of all prime numbers
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


def main():
    # Example usage
    limit = 100
    primes = sieve_of_eratosthenes(limit)
    print(f"Prime numbers up to {limit}: {primes}")


if __name__ == "__main__":
    main()