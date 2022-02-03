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
        x,y=0,0
        for inx in range(len(s)):
            if s[inx-y: inx+1] == s[inx-y: inx+1][::-1]:
                x, y = inx-y, y+1
                print(s[x: x+y])
            elif inx-y > 0 and s[inx-y-1: inx+1] == s[inx-y-1: inx+1][::-1]:
                x, y = inx-y-1, y+2
                print(s[x: x+y])
        return s[x: x+y]