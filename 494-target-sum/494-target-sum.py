class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        visited = {}
        def travel(i, targ):
            if i == len(nums) - 1:
                if nums[i] == targ or nums[i] == -targ:
                    return 1 if targ != 0 else 2
                else:
                    return 0
            
            if (i + 1, targ - nums[i]) not in visited:
                visited[(i + 1, targ - nums[i])] = travel(i + 1, targ - nums[i]) 
            if (i + 1, targ + nums[i]) not in visited:
                visited[(i + 1, targ + nums[i])] = travel(i + 1, targ + nums[i])
            
            
            return visited[(i + 1, targ - nums[i])] + visited[(i + 1 , targ + nums[i])]
        
        return travel(0, target)
            