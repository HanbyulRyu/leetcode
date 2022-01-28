class Solution:
#    def longestPalindrome(self, s: str) -> str:
#        tempArray = []
#        right = left = 0
#        lookup = [[False for _ in range(len(s))] for _ in range(len(s)+1)]
#        
#        for i in range(len(s)):
#            for j in range(i):
#                lookup[j][i] = (s[i] == s[j]) and (i-j<=2 or lookup[j+1][i-1])
#                    
#                if lookup[j][i]:
#                    if i-j > right-left:
#                        left = j
#                        right = i
#              
#        result = s[left:right-left+1]
#        print("left", left, "right", right, "result", result)
#        return result

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l]
                
            
            
                
            
        