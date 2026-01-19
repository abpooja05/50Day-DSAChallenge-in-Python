class Solution:
    def kthElement(self, a, b, k):
        n, m = len(a), len(b)

        # Always binary search on smaller array
        if n > m:
            return self.kthElement(b, a, k)

        low = max(0, k - m)
        high = min(k, n)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            left1 = a[cut1 - 1] if cut1 > 0 else float('-inf')
            left2 = b[cut2 - 1] if cut2 > 0 else float('-inf')

            right1 = a[cut1] if cut1 < n else float('inf')
            right2 = b[cut2] if cut2 < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
