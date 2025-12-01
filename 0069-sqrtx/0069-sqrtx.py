class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x   # sqrt(0)=0, sqrt(1)=1

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        # right will be the floor(sqrt(x))
        return right
