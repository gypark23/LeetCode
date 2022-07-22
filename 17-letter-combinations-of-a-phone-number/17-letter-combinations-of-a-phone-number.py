class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        ret = []
        _map = {}
        _map["2"] = ("a","b","c")
        _map["3"] = ("d", "e", "f")
        _map["4"] = ("g", "h", "i")
        _map["5"] = ("j", "k", "l")
        _map["6"] = ("m", "n", "o")
        _map["7"] = ("p", "q", "r", "s")
        _map["8"] = ("t", "u", "v")
        _map["9"] = ("w", "x", "y", "z")
        
        def dfs(i, path):
            if i >= len(digits):
                ret.append(path[:])
                return
            
            for letter in _map[digits[i]]:
                path += letter
                dfs(i + 1, path[:])
                path = path[:-1]
                
        dfs(0, "")
        return ret
            
            