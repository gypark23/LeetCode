class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def dfs(i, path, targ):
            if targ == target:
                ret.append(path)
                return
            
            if targ > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            dfs(i, path[:], targ + candidates[i])
            path.pop()
            dfs(i + 1, path[:], targ)
            
        dfs(0, [], 0)
        return ret