#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        n = str(N)
        count = 0
        for i in n:
            if int(i) == 0:
                continue
            elif N % int(i) == 0:
                count += 1
        return count
        