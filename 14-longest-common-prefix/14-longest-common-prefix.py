class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        # 문자열이 작은 순으로 정렬 ['flow', 'flower', 'flight']
        strs = sorted(strs, key=len)
        
        # 제일 짧은 문자열을 기준으로 계산 (prefix 이기 때문에)
        standard = strs[0]
        strs = strs[1:len(strs)]
        
        # 제일 짧은 문자열길이가 0 인 경우 "" 리턴
        if len(standard) <= 0:
            return ""

        # standard 기준으로 동일한 문자열 ['flower', 'flight'] -> ['flow', 'fl']
        output = []
        min = 0
        for i in range(len(strs)):
            temp = ""
            for s in range(len(standard)) :
                if standard[s] == strs[i][s]:
                    temp += standard[s]
                else:
                    break
            output.append(temp)
                    
        # 문자열이 가장 짧은 문자
        return sorted(output, key=len)[0]
