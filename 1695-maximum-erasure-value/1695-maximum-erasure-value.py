class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        low = 0
        _maxsum = 0
        _sum = 0
        dic = {}
        
        for high in range(len(nums)):
            _sum += nums[high]
            while(nums[high] in dic):
                _sum -= nums[low]
                del(dic[nums[low]])
                low += 1
            dic[nums[high]] = 1
            _maxsum = max(_maxsum, _sum)
            
        return _maxsum