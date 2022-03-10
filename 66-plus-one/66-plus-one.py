class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        
        i = len(digits)
        temp = 0
        while i > 0:
            if len(digits) == i:
                output = [(digits[i-1] + 1) % 10]
                temp = (digits[i-1] + 1) // 10
            elif temp > 0:
                output = [(digits[i-1] + temp) % 10] + output
                temp = (digits[i-1] + temp) // 10
            else:
                output = [digits[i-1]] + output
            i -= 1
            
        if temp > 0:
            output = [1] + output
            
        return output
                
            
            
        