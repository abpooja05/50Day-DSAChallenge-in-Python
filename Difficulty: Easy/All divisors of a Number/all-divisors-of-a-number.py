
#User function Template for python3

class Solution:
    def print_divisors(self, N):
        smaller = []
        larger = []
        
        i = 1
        while i * i <= N:
            if N % i == 0:
                smaller.append(i)
                if i != N // i:  #avoids duplicating the middle divisor when N is a perfect square.
                    larger.append(N // i)
            i += 1
        
        for num in smaller:
            print(num, end=" ")
        for num in reversed(larger):
            print(num, end=" ")
        