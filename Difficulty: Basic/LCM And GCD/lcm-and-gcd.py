class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        mul = a*b
        while b != 0:
            a, b = b, a%b
            res = [mul//a, a]
        return res