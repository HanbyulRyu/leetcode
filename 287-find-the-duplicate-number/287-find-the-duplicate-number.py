class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        contain = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            if contain[nums[i]] == 1:
                return nums[i]
            else:
                contain[nums[i]] = 1
        