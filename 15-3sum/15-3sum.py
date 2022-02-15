class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        if len(nums) < 3:
            return output

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sumN = nums[i] + nums[left] + nums[right]
                
                if sumN > 0:
                    right -= 1
                elif sumN < 0:
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
            
        return output
                        
#         i = 0
#         while i < len(nums)-2:
#             j = i + 1
#             while j < len(nums)-1:
#                 k = j + 1
#                 while k < len(nums):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result.append(tuple(sorted([nums[i], nums[j], nums[k]])))
#                     k += 1
#                 j += 1
#             i += 1
        
#         중복제거
#         for t in list(set(tuple(result))):
#             output.append(list(t))

#         #print(output)
#         return output