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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root
        queue = [curr]
        idx,threshold = 0, 2
        
        while(queue or curr):
            idx += 1
            curr = queue.pop(0)
            if(not curr):
                break
            if(idx == threshold - 1):
                curr.next = None
                threshold *= 2

            else:
                curr.next = queue[0]
            queue.append(curr.left)
            queue.append(curr.right)
        
        return root