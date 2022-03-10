class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = maxSum = nums[0]
        
        for i in nums[1:]:
            #print(i, current, maxSum)
            current = max(i, current + i)
            maxSum = max(maxSum, current)
            
        return maxSum
            
        
        