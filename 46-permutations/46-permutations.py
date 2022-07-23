class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def backtrack(path, nums):
            if not nums:
                ret.append(path)
                return
            
            for i in range(len(nums)):
                temp = nums[:]
                path.append(nums[i])
                temp.pop(i)
                backtrack(path[:], temp[:])
                path.pop()
        
        backtrack([], nums)
        return ret