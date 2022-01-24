class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentIndex = 0
        resultArray = []
        resultArray.append([])
        maxSize = 0
        
        for s1 in s:
            #print("s1", s1)
            #print("resultArray", resultArray[currentIndex])
            
            if s1 in resultArray[currentIndex]:
                findIndex = resultArray[currentIndex].index(s1)
                tempArray = resultArray[currentIndex][findIndex +1 :len(resultArray[currentIndex])]
                
                resultArray.append([])
                currentIndex += 1
                resultArray[currentIndex] = tempArray
                resultArray[currentIndex].append(s1)
                #print("if", resultArray[currentIndex])
            else:
                resultArray[currentIndex].append(s1)
                #print("else", resultArray[currentIndex])
                
                
        for a1 in resultArray:
            if maxSize < len(a1):
                maxSize = len(a1)
                
        return maxSize