class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """count sort"""
        count = [0] * 3
        for num in nums:
            count[num] += 1
        temp = [0, 1, 2]
        i = 0
        j = 0
        while i < 3:
            while count[i] != 0:
                nums[j] = temp[i]
                j += 1
                count[i] -= 1
            i += 1