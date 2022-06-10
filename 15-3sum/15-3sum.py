class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        print(nums)
        for i, a in enumerate(nums):
            if(i > 0 and nums[i - 1] == a):
                continue
            
            low, high = i + 1, len(nums) - 1
            
            while(low < high):
                if(nums[low] + nums[high] == -a):
                    ret.append([a, nums[low], nums[high]])
                    low += 1
                    while(low < high and nums[low - 1] == nums[low]):
                        low += 1
                elif(nums[low] + nums[high] < -a):
                    low += 1
                else:
                    high -= 1
        
        return ret
                    