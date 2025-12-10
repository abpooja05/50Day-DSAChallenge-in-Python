class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_range = len(nums)+1
        num_set = set(nums)

        for num in range(0, num_range):
            if num not in num_set:
                return num
        return -1