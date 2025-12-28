class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 2
        
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        
        if k >= 0:
            l = len(nums) - 1
            while l > k and nums[l] <= nums[k]:
                l -= 1
                
            nums[k], nums[l] = nums[l], nums[k]
        
        left, right = k + 1, len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        