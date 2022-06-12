class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums) - 3):
            if(i > 0 and nums[i - 1] == nums[i]):
                continue
            for j in range(i + 1, len(nums) - 2):
                if(j != i + 1 and nums[j - 1] == nums[j]):
                    continue
                targ = target - nums[i] - nums[j]
                low, high = j + 1, len(nums) - 1
                while(low < high):
                    _sum = nums[low] + nums[high]
                    if(_sum == targ):
                        ret.append([nums[i], nums[j], nums[low], nums[high]])
                        low += 1
                        while(low < high and nums[low - 1] == nums[low]):
                            low += 1
                    elif(_sum < targ):
                        low += 1
                    else:
                        high -= 1
        
        return ret
                        