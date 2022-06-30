from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        low = 0
        dq = deque()
        ret = []
        for high in range(0, len(nums)):
            while(dq and nums[dq[-1]] < nums[high]):
                dq.pop()
            dq.append(high)
            if(high - low == k - 1):
                ret.append(nums[dq[0]])
                if(low == dq[0]):
                    #print(low)
                    dq.popleft()
                low += 1
        return ret