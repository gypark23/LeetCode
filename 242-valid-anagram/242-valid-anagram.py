class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = [0] * 26
        dic_t = [0] * 26
        
        for char in s:
            dic_s[ord(char) - ord('a')] += 1
        for char in t:
            dic_t[ord(char) - ord('a')] += 1
        
        return dic_s == dic_t