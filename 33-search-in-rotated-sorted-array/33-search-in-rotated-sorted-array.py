class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while(low <= high):
            mid = (low + high) // 2
            print(low, mid, high)
            if(nums[mid] == target):
                return mid
            #any numbers before nums[mid] sorted
            if(nums[low] <= nums[mid]):
                if(target >= nums[low] and target <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            #any numbers after nums[mid] sorted
            #[7,-1,1,2,3]
            else:
                if(target <= nums[high] and target >= nums[mid]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
                