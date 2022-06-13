class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        low, diff, mindiff = 0, 0, 10**5
        minsum = 3001
        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            print(i, low, high)
            while(low < high):
                _sum = nums[low] + nums[high] + nums[i]
                if(_sum == target):
                    return target
                elif(_sum > target):
                    if(mindiff > abs(target - _sum)):
                        mindiff = abs(target - _sum)
                        minsum = _sum
                    high -= 1
                else:
                    if(mindiff > abs(target - _sum)):
                        mindiff = abs(target - _sum)
                        minsum = _sum
                    low += 1
        return minsum
                    
        