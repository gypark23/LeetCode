class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while(low <= high):
            mid = (low + high) // 2
            print(low, mid, high)
            if(nums[mid] == target):
                return mid
            #any numbers after nums[mid] sorted
            if(nums[low] <= nums[mid]):
                if(target > nums[mid] or target < nums[low]):
                    low = mid + 1
                else:
                    high = mid - 1
            
            #any numbers before nums[mid] sorted
            else:
                if(target < nums[mid] or target > nums[high]):
                    high = mid - 1
                else:
                    low = mid + 1
 
        return -1
                