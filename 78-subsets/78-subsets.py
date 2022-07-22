class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def dfs(i, path):
            if i == len(nums):
                ret.append(path)
                return
            
            path.append(nums[i])
            dfs(i + 1, path[:])
            path.pop()
            dfs(i + 1, path[:])
        
        dfs(0, [])
        return ret
            