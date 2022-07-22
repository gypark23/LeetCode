class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ret = []
        for i in range(len(nums)):
            before = [nums[i]]
            temp = nums[:]
            temp.pop(i)
            perms = self.permute(temp)
            for perm in perms:
                ret.append(before + perm)
        
        return ret
            
            