class Solution:
    def countAndSay(self, n: int) -> str:
        answer = '1'
        
        if n == 1:
            return answer
        
        for i in range(n-1):
            result = ''
            j = 0
            while j < len(answer):
                count = 1
                while j + 1 < len(answer) and answer[j] == answer[j+1]:
                    count += 1
                    j += 1
                result = result + str(count) + str(answer[j])
                j += 1
            answer = result
            
        return answer
            
            