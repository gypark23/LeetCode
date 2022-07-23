class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        def backtrack(i, path):
            if i == len(nums):
                ret.append(path[:])
                return
            
            #option 1, include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path[:])
            path.pop()
            #option 2, do not include nums[i] at all
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, path[:])
            
        backtrack(0, [])
        return ret