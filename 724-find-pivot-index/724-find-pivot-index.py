class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        _firstsum = 0
        for i in range(len(nums)):
            _sum -= nums[i]
            if(_firstsum == _sum):
                return i
            _firstsum += nums[i]
        return -1