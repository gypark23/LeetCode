class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        
        def backtrack(path, lefts, rights):
            if lefts == 0 and rights == 0:
                ret.append(path[:])
                return
            
            if lefts < 0 or rights < 0:
                return
            
            flag = False
            
            if lefts >= 1:
                path += "("
                backtrack(path[:], lefts - 1, rights)
                flag = True
            if rights > lefts and rights >= 1:
                path = path[:-1] + ")" if flag else path + ")"
                backtrack(path[:], lefts, rights - 1)
            
        backtrack("", n, n)
        
        return ret
            
            