#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        first = n % 10
        second = (n // 10) % 10
        third = n // 100
        
        digit_sum = first ** 3 + second ** 3 + third ** 3

        return n == digit_sum