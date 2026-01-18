class Solution:
    def inversionCount(self, arr):
        # Your Code Here
        # Function to use modified merge sort to count inversions
        def merge_sort(arr, temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2
                inv_count += merge_sort(arr, temp, left, mid)
                inv_count += merge_sort(arr, temp, mid + 1, right)
                inv_count += merge(arr, temp, left, mid, right)
            return inv_count
        
        def merge(arr, temp, left, mid, right):
            inv_count = 0
            i = left  # Starting index for left subarray
            j = mid + 1  # Starting index for right subarray
            k = left  # Starting index to be sorted
            
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1
            
            # Copy the remaining elements of left subarray
            while i <= mid:
                temp[k] = arr[i]
                k += 1
                i += 1
            
            # Copy the remaining elements of right subarray
            while j <= right:
                temp[k] = arr[j]
                k += 1
                j += 1
            
            # Copy the sorted subarray back to original array
            for idx in range(left, right + 1):
                arr[idx] = temp[idx]
            
            return inv_count
        
        n = len(arr)
        temp = [0] * n
        return merge_sort(arr, temp, 0, n - 1)