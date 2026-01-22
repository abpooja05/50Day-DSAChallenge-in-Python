class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        candidate = 0
        
        # Find the potential celebrity
        for i in range(1, n):
            if mat[candidate][i] == 1:
                candidate = i
        
        # Verify the candidate
        for i in range(n):
            if i != candidate and (mat[i][candidate] == 0 or mat[candidate][i] == 1):
                return -1
        
        return candidate