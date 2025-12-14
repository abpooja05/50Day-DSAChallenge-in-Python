class Solution:
    def nthRowOfPascalTriangle(self, n):
        if n == 1  :
            tmp = [1]
            return tmp;

        tans = self.nthRowOfPascalTriangle(n-1);
        
        ans = []
        ans.append(1);

        for i in range(1,len(tans)) :
            ans.append((tans[i]+tans[i-1])%1000000007)
        
        ans.append(1)

        return ans


       