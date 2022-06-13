class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low, maxf, ret = 0, 0, 0
        dic = {}
        for high in range(len(s)):
            dic[s[high]] = dic.get(s[high], 0) + 1
            maxf = max(maxf, dic[s[high]])
            
            if(high - low + 1 - maxf > k):
                dic[s[low]] -= 1
                low += 1
            else:
                ret = max(ret, high - low + 1)
        return ret