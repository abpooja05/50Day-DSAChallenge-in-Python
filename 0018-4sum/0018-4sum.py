class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to facilitate the two-pointer approach
        n = len(nums)
        quadruplets = []

        for i in range(n - 3):  # Fix the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element

            for j in range(i + 1, n - 2):  # Fix the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for the second element

                left, right = j + 1, n - 1  # Initialize two pointers for the third and fourth elements

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # Skip duplicates for the third element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # Skip duplicates for the fourth element

                        left += 1
                        right -= 1

                    elif current_sum < target:
                        left += 1  # Move the left pointer to the right to increase the sum
                    else:
                        right -= 1  # Move the right pointer to the left to decrease the sum

        return quadruplets