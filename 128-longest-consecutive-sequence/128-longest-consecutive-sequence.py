class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0
        ret = 0
        for num in numset:
            if(num - 1 in numset):
                continue
            count = 1
            while(num + count in numset):
                count += 1
            ret = max(ret, count)
        
        return ret