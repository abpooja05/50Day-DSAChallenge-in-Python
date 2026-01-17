class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_counts = {0: 1}  # To handle the case where a prefix sum itself equals k

        for num in nums:
            prefix_sum += num
        
        # Check if there exists a prefix_sum such that current_prefix_sum - prefix_sum = k
            if (prefix_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[prefix_sum - k]
        
        # Update the hashmap with the current prefix_sum
            if prefix_sum in prefix_sum_counts:
                prefix_sum_counts[prefix_sum] += 1
            else:
                prefix_sum_counts[prefix_sum] = 1

        return count

        