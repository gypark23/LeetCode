import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            distance = sqrt(point[0] **2 + point[1] ** 2)
            heappush(heap, (-distance, point[0], point[1]))
            while len(heap) > k:
                heappop(heap)
        ret = []
        for i in range(k):
            ret.append([heap[0][1], heap[0][2]])
            heappop(heap)
        return ret