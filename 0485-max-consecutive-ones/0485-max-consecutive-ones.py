class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maxm = 0
        for i in nums:
            if i ==1:
                current += 1
            if current>maxm:
                maxm=current
            if i==0:
                current=0
        return maxm