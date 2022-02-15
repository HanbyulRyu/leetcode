class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        output = (right-left)*min(height[right], height[left])
        
        while right - left > 0:
            output = max(output, (right-left)*min(height[right], height[left]))
            #print(output)
            
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
                
        return output
                
            