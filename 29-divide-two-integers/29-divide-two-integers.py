class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
#         result = int(dividend/divisor)
        
#         if result > 2**31-1:
#             return 2**31-1
#         elif result < -2**31:
#             return -2**31
        
#         return result
        if divisor == 1:
            return dividend
        if dividend == divisor:
            return 1
       
        max = (2**31)-1
        if divisor == -1:
            if dividend > max + 1:
                return -(max + 1)
            if dividend < -max:
                return max
            return -dividend
  
        sign = True
        if dividend < 0:
            dividend = -dividend
            sign = not sign
        if divisor < 0:
            divisor = -divisor
            sign = not sign

        temp = divisor
        
        # dividen 큰 거듭제곱 수를 구한다. (dividend = 16, divisor = 3, exp = 3, temp = 27)
        exp = 0
        while dividend >= temp:
            exp += 1
            temp = divisor**exp
        
        # epx 에서 1을 빼주고 하나 작은 거듭제곱을 구함 (dividend = 16, divisor = 3, exp = 2, temp = 9)
        exp -= 1
        temp = divisor**exp
        
        result = 0
        while dividend >= divisor:
            # 하나 작은 거듭제곱부터 시작하여 거듭제곱을 줄여가면서 dividend 에서 빼준다. (temp 가 divisor가 되면 exp는 1에서 고정되서 횟수만큼 result 에 더해진다.)
            # (dividen = 7, divisor = 3, exp = 2, result = 3)
            # (dividen = 4, divisor = 3, exp = 1, reulst = 4)
            # (dividen = 1, divisor = 3, exp = 1, result = 4)
            if dividend >= temp:
                dividend -= temp
                result += divisor**(exp-1)
            # 그보다 더 작은 거듭제곱을 빼줄 수 있도록 temp 값을 하나 더 작은 거듭제곱으로 변경 (exp = 1, temp = 3)
            else :
                exp -= 1
                temp = divisor**exp
        
        if sign:
            if(result > 2**31-1):
                return 2**31-1
            return result
        else:
            return -result
            
        
            
        
        