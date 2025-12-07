class Solution:
  def countPrimes(self, n: int) -> int:
    
    if n <= 1:
      return 0
    
    # Initialize a list to mark visited numbers (is_prime[i] = True indicates i is prime)
    is_prime = [True] * n  # n is the size of the array
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Sieve of Eratosthenes to mark non-primes
    for i in range(2, int(n**0.5) + 1):
      if is_prime[i]:
        for j in range(i * i, n, i):
          is_prime[j] = False

    # Count the number of primes
    count = 0
    for num in is_prime:
      if num:
        count += 1

    return count