class Solution:
    def rowWithMax1s(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])
        max_count = 0
        result_row = -1
        
        for i in range(n):
            # Using binary search to find the first occurrence of 1 in the current row
            left, right = 0, m - 1
            first_one = m  # Initialize with the number of columns (no 1s)
            
            while left <= right:
                mid = (left + right) // 2
                if arr[i][mid] == 1:
                    first_one = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            count = m - first_one
            if count > max_count:
                max_count = count
                result_row = i
            elif count == max_count and result_row == -1:
                result_row = i
        
        return result_row if max_count != 0 else -1
