class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        result = ""
        for idx in range(len(s)):
            if len(result) == 0:
                if s[idx] in {'-','+'} or s[idx].isdigit():
                    result += s[idx]
                else:
                    break
            else:
                if s[idx].isdigit():
                    result += s[idx]
                else:
                    break

          
        if len(result) <= 0 or result in {'-','+'}:
            return 0
        elif int(result) > 2**31-1:
            return 2**31-1
        elif int(result) < -2**31:
            return -2**31
        else:
            return int(result)