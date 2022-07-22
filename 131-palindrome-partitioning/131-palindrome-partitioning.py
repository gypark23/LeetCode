class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        
        def isPalindrome(s):
            low, high = 0, len(s) - 1
            while low <= high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True
        
        def backtrack(start, end, path):
            if start >= len(s):
                ret.append(path)
                return
            
            #option 1, split at end
            if isPalindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, end + 1, path[:])
                path.pop()
            
            #option 2, don't split
            if end < len(s):
                backtrack(start, end + 1, path[:])
        
        backtrack(0, 1, [])
        return ret
            
            
            
            