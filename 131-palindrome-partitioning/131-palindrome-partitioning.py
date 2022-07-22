from itertools import permutations

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s):
            return s == s[::-1]
        
        def backtrack(s, left, path, result):
            # print(s, left, path, result)
            if left == len(s):
                result.append(path)
                return
            
            for right in range(left+1, len(s)+1):
                sub = s[left:right]
                if isPalindrome(sub):
                    # print(sub)
                    backtrack(s, right, path+[sub], result)
        
        backtrack(s, 0, [], result)
        return result