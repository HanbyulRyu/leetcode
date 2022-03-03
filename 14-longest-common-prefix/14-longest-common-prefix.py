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
    
        print(strs)
        print(standard)
        # standard 기준으로 min 값 구하기
        # ['flower', 'flight'] -> [1111, 1100]
        min = 0
        for i in range(len(strs)):
            temp = ""
            for s in range(len(standard)) :
                if standard[s] == strs[i][s]:
                    temp += "1"
                else:
                    break
            
            if len(temp) > 0 and i == 0:
                min = int(temp)
                print("i", min)
            elif len(temp) > 0 and min >= int(temp):
                min = int(temp)
                print("elif", min)
            elif len(temp) <= 0:
                return ""

        print(min)
        # min 의 1의 개수만큼 standard 문자열에서 가져온다. 'flow' / 1100 -> 'fl'
        output = ""
        for i in range(len(str(min))):
            if str(min)[i] == "1":
                output += standard[i]
            else:
                break

        return output