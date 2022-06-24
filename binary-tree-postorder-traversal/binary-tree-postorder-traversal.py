# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ret = [], []
        curr = root
        
        while(curr or stack):
            while(curr):
                stack.append((curr, False))
                curr = curr.left
            
            curr, visited = stack.pop()
            if(visited):
                ret.append(curr.val)
                curr = None
            else:
                stack.append((curr, True))
                curr = curr.right
        
        return ret
            