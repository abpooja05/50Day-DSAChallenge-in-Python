from collections import Counter
class Solution:
    def findTwoElement(self, arr):
        # code here
        c = Counter(arr)
        l = len(arr)
        result = [None, None]
        for i in range(1, l+1):
            if c[i] == 2:
                result[0] = i
            elif c[i] == 0:
                result[1] = i
        
        return result