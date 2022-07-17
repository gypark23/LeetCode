from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        queue.append(0)
        visited.add(0)
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True