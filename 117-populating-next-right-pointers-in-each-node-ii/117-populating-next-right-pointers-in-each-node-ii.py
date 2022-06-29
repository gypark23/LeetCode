"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root
        prev = Node(0)
        while(curr):
            if(curr.left):
                prev.next = curr.left
                prev = curr.left
            if(curr.right):
                prev.next = curr.right
                prev = curr.right
            curr = curr.next
        prev.next = None
        
        root.left = self.connect(root.left)
        root.right = self.connect(root.right)
        return root