class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        matched = [False for i in range(len(s)+1)]
        matched[0] = True
        
        for i in range(len(s)):
            for j in range(1, len(s)+1):
                if matched[i] and s[i:j] in wordDict:
                    matched[j] = True

        if matched[-1]:
            return True
        
        return False