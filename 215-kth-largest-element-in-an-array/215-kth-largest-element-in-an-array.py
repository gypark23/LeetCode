import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """nums.sort(reverse = True)
        return nums[k - 1]
        """
        return nlargest(k, nums)[-1]
        