class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        answer = []
        
        for i in range(n):
            if i < 2:
                answer.append(i+1)
            else:
                answer.append(answer[i-2] + answer[i-1])
            
        return answer[n-1]
