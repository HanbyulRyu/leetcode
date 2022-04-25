class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in nums and i != nums.index(gap):
                return [i, nums.index(gap)]

        
        return output
                        