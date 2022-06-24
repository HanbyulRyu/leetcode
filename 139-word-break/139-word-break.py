class Solution:
    # 1 :: replace
        # "cars", ["car","ca","rs"] 인 경우 false
    # 2 :: replace 이지만 이중 for
        # "cbca", ["bc","ca"] 인 경우 true 로 나옴
    # 2-1 :: 처음부터 매칭 안되는 경우 false 로 리턴 처리
        # "abcd", ["a","abc","b","cd"] 인 경우 false 로 나옴
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        matched = [False for i in range(len(s)+1)]
        matched[0] = True
        
        for i in range(len(s)):
            for j in range(1, len(s)+1):
                if matched[i] and s[i:j] in wordDict:
                    # print("matched[",i,"]", "-", s[i:j])
                    # matched[ 0 ] - leet
                    # matched[ 4 ] - code
                    matched[j] = True

        if matched[-1]:
            return True
        
        return False
    
    