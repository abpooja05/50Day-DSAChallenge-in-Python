class Solution:
    def largest(self, arr):
        lar = arr[0]
        for i in range(len(arr)):
            if arr[i]>lar:
                lar=arr[i]
        return lar