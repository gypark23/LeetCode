class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for mid in range(len(s)):
            low, high = mid, mid
            while(low >= 0 and high < len(s) and s[low] == s[high]):
                count += 1
                low -= 1
                high += 1
            
            low, high = mid - 1, mid
            while(low >= 0 and high < len(s) and s[low] == s[high]):
                count += 1
                low -= 1
                high += 1
        
        return count
            