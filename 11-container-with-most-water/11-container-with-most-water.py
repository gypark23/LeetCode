class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        ret = 0
        
        while(low < high):
            ret = max(ret, (high - low) * min(height[high], height[low]))
            if(height[low] <= height[high]):
                low += 1
            else:
                high -= 1
                
        return ret
        