from itertools import permutations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(1, len(nums) + 1):
            result += list(set([tuple(sorted(x)) for x in permutations(nums, i)]))
        
        result.append([])

        return result
                           
       
        