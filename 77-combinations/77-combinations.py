class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        
        
        def backtrack(path, num):
            if len(path) >= k:
                ret.append(path)
                return
            
            if num > n:
                return
            
            #option 1, add num to path
            path.append(num)
            backtrack(path[:], num + 1)
            
            #option 2, do not add num
            path.pop()
            backtrack(path[:], num + 1)
        
        backtrack([], 1)
        return ret