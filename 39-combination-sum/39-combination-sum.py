class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def dfs(i,path,targ):
            if targ == 0:
                ret.append(path[:])
            if targ < 0 or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, path, targ - candidates[j])
                path.pop()
        
        dfs(0, [], target)
        
        return ret
            
            