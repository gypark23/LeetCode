from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        squares = {i ** 2 for i in range(int(sqrt(n)) + 1)}
        queue = deque()
        queue.append(n)
        ret = 0
        while queue:
            size = len(queue)
            for _ in range(size - 1, -1, -1):
                n = queue.popleft()
                if n == 0:
                    return ret
            
                for square in squares:
                    if n - square > 0:
                        queue.append(n - square)
                    elif n - square == 0:
                        return ret + 1
            ret += 1
        
        return ret
        
        