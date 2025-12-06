#User function Template for python3
class Solution:
    def largestPrimeFactor (self, N):
        # code here
        i = 2
        while i*i <= N:
            if N % i == 0:
                N = N // i
            else:
                i += 1
        return N
        
