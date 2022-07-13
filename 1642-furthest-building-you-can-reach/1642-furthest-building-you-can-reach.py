import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        _sum = 0
        #for maximum pq
        #pq.push(height diff), sum += height diff
        #if sum > bricks
        #pq.pop, sum -= height diff, ladders -= 1
        #continue until ladders = 0, sum > bricks
        #return index - 1 if break within loop, else index
        i = 0
        for i in range(1, len(heights)):
            diff = heights[i - 1] - heights[i]
            if diff < 0:
                heappush(pq, diff)
                _sum -= diff
            if _sum > bricks:
                if ladders == 0:
                    return i - 1
                max_diff = heappop(pq)
                _sum += max_diff
                ladders -= 1
        return i