class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in dic:
                dic[sorted_string].append(string)
            else:
                dic[sorted_string] = [string]
        
        return dic.values()