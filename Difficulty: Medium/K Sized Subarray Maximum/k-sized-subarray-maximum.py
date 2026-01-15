from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        if not arr:
            return []
        if k == 1:
            return arr
        
        q = deque()
        result = []
        
        for i in range(k):
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
        
        for i in range(k, len(arr)):
            result.append(arr[q[0]])
            
            while q and q[0] <= i - k:
                q.popleft()
            
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
        
        result.append(arr[q[0]])
        return result