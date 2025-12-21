class Solution:
    def check(self, nums: List[int]) -> bool:
        maxNum, minNum, minIdx = max(nums), min(nums), 0
        for i in range(1, len(nums)):
            if [nums[i-1], nums[i]] == [maxNum, minNum]:
                minIdx = i                
                break
        return nums[minIdx:] + nums[:minIdx] == sorted(nums)



    