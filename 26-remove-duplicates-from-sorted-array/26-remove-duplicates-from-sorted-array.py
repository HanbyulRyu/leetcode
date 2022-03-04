class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) > 1:
                nums.remove(num)
            
        return len(nums)