class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend/divisor)
        
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        
        return result
        