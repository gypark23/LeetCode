class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 0
        
        for high in range(1, len(nums)):
            if(nums[high] == nums[high - 1]):
                continue
            low += 1
            nums[low] = nums[high]
        
        return low + 1