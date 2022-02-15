class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)
        result = 0
        
        if length % 2 == 0:
            result = (merged[int(length / 2 - 1)] +  merged[int(length / 2)]) / 2
        else:
            result = merged[int(length/2)]
            
        return result
            
        