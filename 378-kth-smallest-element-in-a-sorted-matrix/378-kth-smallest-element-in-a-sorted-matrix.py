import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for i in range(len(matrix)):
            heappush(heap, (matrix[i][0], i, 0))
        
        while k:
            val, i, j = heappop(heap)
            if j + 1 < len(matrix):
                heappush(heap, (matrix[i][j + 1], i, j + 1))
            k -= 1
        
        return val