"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(not root):
            return None
        
        queue = deque()
        queue.append(root)
        curr = root
        
        while(queue):
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if(i != size - 1):
                    curr.next = queue[0]
                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)
        return root