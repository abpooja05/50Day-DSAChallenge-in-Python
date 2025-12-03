#User function Template for python3


class Solution:
    def isDigitSumPalindrome(self, n):
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n = n // 10
            
        digit_sum_str = str(digit_sum)
        
        if digit_sum_str == digit_sum_str[::-1]:
            return 1
        else:
            return 0
            
