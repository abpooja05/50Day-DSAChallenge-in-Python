#User function Template for python3

class Solution:
    def prime_Sum(self, n):
        if n<=1:
            return 0

        # sieve of eratosthenes algo-A value in prime[i] will
        # finally be false if i is Not a prime, true if i is a prime
        prime = [True] * (n+1)
        
        prime[0] = False   # as 0 and 1 are nonprime numbers
        prime[1] = False
        
        i = 2
        while i*i<=n:
            if prime[i]:
                j = i*i
                while j<=n:
                    prime[j] = False  
                    j += i
            i += 1
            
        
        # Sum all prime numbers
        sum = 0
        for p in range(2, n+1):
            if prime[p]:
                sum += p

        return sum
