class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums) - 1
        ret = [0] * len(nums)
        idx = len(nums) - 1
        while(low <= high):
            if(abs(nums[low]) > abs(nums[high])):
                ret[idx] = (nums[low] * nums[low])
                low += 1
                idx -= 1
            else:
                ret[idx] = (nums[high] * nums[high])
                high -= 1
                idx -= 1
        
        return ret