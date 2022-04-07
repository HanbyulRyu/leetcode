class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        while left <= right :
            mid = left + (right - left) // 2
            
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                break
                
        if nums[mid] != target:
            return [-1, -1]
            
        left = mid
        while left > 0 and nums[left-1] == target:
            left = left - 1
            
        right = mid
        while right < len(nums) - 1 and nums[right+1] == target:
            right = right + 1
                    
        
        return [left, right]
            
                
                    