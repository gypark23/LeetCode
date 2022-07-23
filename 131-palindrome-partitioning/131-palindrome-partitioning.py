class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def isPalindrome(low, high):
            while low <= high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            
            return True
        
        def backtrack(path, start, end):
            if start >= len(s):
                ret.append(path)
                return

            
            #option 1, split at end
            if isPalindrome(start, end - 1):
                path.append(s[start:end])
                backtrack(path[:], end, end + 1)
                path.pop()
            
            #option 2, don't split
            if end < len(s):
                backtrack(path[:], start, end + 1)
            
        backtrack([], 0, 1)
        return ret

            
            