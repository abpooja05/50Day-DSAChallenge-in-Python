#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        if s1 == "0" or s2 == "0":
            return "0"

        sign = 1
        if s1[0] == '-':
            sign *= -1
            s1 = s1[1:]
        if s2[0] == '-':
            sign *= -1
            s2 = s2[1:]

        m = len(s1)
        n = len(s2)
        result = [0] * (m + n)  # Initialize result array with zeros

        # Perform digit-by-digit multiplication using nested loops
        for i in range(m - 1, -1, -1):
            digit1 = int(s1[i])
            carry = 0
            for j in range(n - 1, -1, -1):
                digit2 = int(s2[j])
                product = digit1 * digit2 + result[i + j + 1] + carry
                carry = product // 10
                result[i + j + 1] = product % 10
            if carry > 0:
                result[i] += carry

        # Remove leading zeros from the result
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1

        # Handle negative sign and convert result to string
        result_str = ''.join(str(digit) for digit in result[i:])
        return (('-' if sign == -1 else '') + result_str) if result_str else "0"

