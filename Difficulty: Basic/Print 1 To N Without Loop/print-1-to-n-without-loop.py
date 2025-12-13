class Solution:    
    def printNos(self,n):
        #Code here
        if n == 0:
            return
        else:
            self.printNos(n-1)
            print(n, end=" ")
        

