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
        head = root
        dummy = Node(0)
        while(head):
            curr = head
            prev = dummy
            while(curr):
                if(curr.left):
                    prev.next = curr.left
                    prev = curr.left
                if(curr.right):
                    prev.next = curr.right
                    prev = curr.right
                curr = curr.next
            head = dummy.next
            dummy.next = None
        
        return root