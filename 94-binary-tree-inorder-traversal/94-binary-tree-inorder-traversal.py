# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        ret = []
        
        while(stack or curr):
            if(curr):
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ret.append(curr.val)
                curr = curr.right
        
        return ret