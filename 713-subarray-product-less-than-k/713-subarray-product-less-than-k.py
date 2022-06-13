class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        low = 0
        ret = 0
        mult = 1
        for high in range(len(nums)):
            mult *= nums[high]
            while(low <= high and mult >= k):
                mult /= nums[low]
                low += 1
            
            ret += (high - low + 1)
        
        return ret