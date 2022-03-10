class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #o(N)
        #return nums.index(target)
    
        #o(log n)
        left = 0
        right = len(nums)
        
        position = -1
        while left < right :
            mid = left + (right - left) // 2
            #print("left :", left, ", mid :", mid, ", right :", right)
            #print("nums[left] :", nums[left], ", nums[mid] :", nums[mid], ", nums[right] :", nums[right-1])
            
            # left : 0 , mid : 3 , right : 6
            # nums[left] : 4 , nums[mid] : 7 , nums[right] : 2
            
            # left : 3 , mid : 4 , right : 6
            # nums[left] : 7 , nums[mid] : 0 , nums[right] : 2
            
            if nums[mid] == target:
                position = mid
                break
            
            if nums[left] < nums[mid]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target and nums[right-1] >= target:
                    left = mid
                else:
                    right = mid
            
        return position

                
        