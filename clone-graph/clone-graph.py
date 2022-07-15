"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def clone(n):
            if not n:
                return None
            
            ret = Node(n.val)
            visited[n.val] = ret
            neighbors = []
            for neighbor in n.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = clone(neighbor)
                neighbors.append(visited[neighbor.val])
            ret.neighbors = neighbors
            
            return ret
    
        return clone(node)