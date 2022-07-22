class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        def dfs(i, path, _sum):         
            if _sum == target:
                ret.append(path[:])
                return
            
            if i >= len(nums) or _sum > target:
                return
            
            path.append(nums[i])
            dfs(i + 1, path, _sum + nums[i])
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path, _sum)
        
        dfs(0, [], 0)
        return ret
            