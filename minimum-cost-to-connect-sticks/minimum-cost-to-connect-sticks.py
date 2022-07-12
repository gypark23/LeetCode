import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        ret = 0
        for stick in sticks:
            heappush(heap, stick)
        while len(heap) > 1:
            first = heappop(heap)
            second = heappop(heap)
            ret += (first + second)
            heappush(heap, first + second)
        
        return ret
        