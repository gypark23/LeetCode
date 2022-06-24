# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return None
        
        ret, queue = [], []
        curr = root
        
        queue.append(curr)
        while(queue):
            floor, size = [], len(queue)
            for i in range(size):
                curr = queue.pop(0)
                floor.append(curr.val)
                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)
            ret.append(floor)
        
        return ret
            
        