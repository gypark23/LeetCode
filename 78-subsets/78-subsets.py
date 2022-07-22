class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        
        def backtrack(i, path):
            if i == len(nums):
                return
            
            path.append(nums[i])
            ret.append(path)
            
            for j in range(i, len(nums)):
                backtrack(j + 1, path[:])
        
        for i in range(len(nums)):
            backtrack(i, [])
        return ret