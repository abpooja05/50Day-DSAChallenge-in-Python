#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        if n > 0:
            print(n, end=" ")
            self.printNos(n-1)
