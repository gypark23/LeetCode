class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        dic_list = list(dic.items())
        dic_list.sort(key = lambda x: x[1], reverse = True)
        for i in range(k):
            ret.append(dic_list[i][0])
        
        return ret