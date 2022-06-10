class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        low = 0
        maxsum = 0
        _sum = 0
        for high in range(len(fruits)):
            dic[fruits[high]] = 1 + dic.get(fruits[high], 0)
            _sum += 1
            while(len(dic) > 2):  
                if(dic[fruits[low]] > 1):
                    dic[fruits[low]] -= 1
                else:
                    del dic[fruits[low]]
                low += 1
                _sum -= 1
            maxsum = max(maxsum, _sum)
        
        return maxsum