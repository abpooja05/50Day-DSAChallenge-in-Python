class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        # Sort the input list
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first element
                continue

            left, right = i + 1, n - 1
            while left < right:
            # Calculate the sum
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Add the triplet to results
                    result.append([nums[i], nums[left], nums[right]])
                    # Move pointers to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                # Move left pointer to increase sum
                    left += 1
                else:
                # Move right pointer to decrease sum
                    right -= 1

        return result