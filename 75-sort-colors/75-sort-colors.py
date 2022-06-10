class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """count sort
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
        """
        
        """three pointers"""
        
        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        
        low, mid, high = 0, 0, len(nums) - 1
        
        while(mid <= high):
            if(nums[mid] == 0):
                swap(mid, low)
                low += 1
                mid += 1
            elif(nums[mid] == 2):
                swap(mid, high)
                high -= 1
            else:
                mid += 1
            
            
        
        
            