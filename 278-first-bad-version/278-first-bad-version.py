# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low, high = 1, n
        
        if(high == 1):
            return 1
        
        while(low <= high):
            mid = (low + high) // 2
            print(low, mid, high)
            if(isBadVersion(mid) != isBadVersion(mid + 1)):
                return mid + 1
            if(isBadVersion(mid - 1) != isBadVersion(mid)):
                return mid
            if(isBadVersion(mid)):
                high = mid - 1
            else:
                low = mid + 1
                
        #f t t
        return -1
            