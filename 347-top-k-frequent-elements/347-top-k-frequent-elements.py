class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
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
        """
        
        ret = []
        dic = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            dic[c].append(n)
         
        for i in range(len(dic) - 1, -1, -1):
            for n in dic[i]:
                ret.append(n)
                if(len(ret) == k):
                    return ret