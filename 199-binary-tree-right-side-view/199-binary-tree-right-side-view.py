# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return None
        
        queue = deque()
        queue.append(root)
        ret = []
        
        while(queue):
            ret.append(queue[-1].val)
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)
        
        return ret
                
        