class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        if(high == 0):
            return nums[0]
        while(low < high):
            mid = (low + high) // 2
            print(low, mid, high)
            if(high == low):
                return nums[low]
            
            if(nums[mid] > nums[mid + 1]):
                return nums[mid + 1]
            
            if(nums[mid - 1] > nums[mid]):
                return nums[mid]
            
            if(nums[mid] > nums[low] and nums[mid] > nums[high]):
                low = mid + 1
            #nums[mid] < nums[low]
            else:
                high = mid - 1
        """
        [4,5,6,7,8,0,1]
        [4,5,7,0,1,2,3]
        """
        return nums[low]
            