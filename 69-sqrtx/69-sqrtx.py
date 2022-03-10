class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while left <= right:
            mid = (left + right) // 2
            multi = mid * mid
            if multi == x:
                return mid
            elif multi > x:
                right = mid - 1
            else:
                left = mid + 1

        return right