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
        for idx in range(len(s)):
            #print("index=",idx,",x =",x,",y =",y)
            #print("1 || s[",idx-y,":",idx+1,"] == s[",idx-y,":",idx+1,"][::-1] ->",s[idx-y: idx+1],"==",s[idx-y: idx+1][::-1])
            #if idx-y > 0:
                #print("2 || s[",idx-y-1,":",idx+1,"] == s[",idx-y-1,":",idx+1,"][::-1] ->",s[idx-y-1: idx+1],"==",s[idx-y-1: idx+1][::-1])
            if s[idx-y: idx+1] == s[idx-y: idx+1][::-1]:
                x, y = idx-y, y+1
                #print("1-1 || x =",x," y =",y)
                #print("1-2 || s[",x,":",x,"+",y,"] = ", s[x: x+y])
            elif idx-y > 0 and s[idx-y-1: idx+1] == s[idx-y-1: idx+1][::-1]:
                x, y = idx-y-1, y+2
                #print("2-1 || x = ",x," y = ",y)
                #print("2-2 || s[",x,":",x,"+",y,"] = ", s[x: x+y])
        return s[x: x+y]