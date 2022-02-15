class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            gap = target - nums[i]
            j = i + 1
            
            while j < len(nums):
                if nums[j] == gap:
                    output = [i, j]
                    break
                j += 1
        
        return output
                        