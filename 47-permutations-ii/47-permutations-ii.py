class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        def backtrack(path, nums):
            if not nums:
                ret.append(path[:])
                return
            
            prev = -20
            for i, num in enumerate(nums):
                if num == prev:
                    continue
                path.append(num)
                temp = nums[:]
                temp.pop(i)
                backtrack(path, temp[:])
                path.pop()
                prev = num
        
        backtrack([], nums)
        return ret
                
                