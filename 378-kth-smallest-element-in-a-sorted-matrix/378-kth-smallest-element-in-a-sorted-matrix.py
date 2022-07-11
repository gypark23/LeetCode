import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for row in matrix:
            for col in row:
                heappush(heap, -col)
                while(len(heap) > k):
                    heappop(heap)
        
        return -heappop(heap)