import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ret = 0
        heap = []
        
        intervals.sort(key = lambda x: x[0])
        
        for elem in intervals:
            #new meeting time is after the first-ending meeting, therefore pop
            if heap and elem[0] >= heap[0][0]:
                heappop(heap)
            heappush(heap, (elem[1], elem[0]))
            ret = max(ret, len(heap))
        
        return ret
                
            