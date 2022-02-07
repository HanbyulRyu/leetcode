class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        result = 0
        if len(strX) <= 1:
            return strX
        elif strX[0].isdigit():
            result = int(strX[::-1].lstrip("0"))
        else:
            temp = strX[0]
            result = int(temp + strX[1:len(strX)][::-1].lstrip("0"))
            
        if result > 2**31-1 or result < -2**31:
            return 0
        else:
            return result
        