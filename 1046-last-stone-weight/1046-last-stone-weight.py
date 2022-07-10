import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]
        heapify(stones)
        while(len(stones) > 1):
            first = heappop(stones) * -1
            second = heappop(stones) * -1
            if first - second > 0:
                heappush(stones, -(first - second))
        
        return -stones[0] if stones else 0
        
        