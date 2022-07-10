# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def travel(r):
            if not r:
                return True, 0
            
            l_b, l_h = travel(r.left)
            r_b, r_h = travel(r.right)
            
            return (l_b and r_b) and (abs(l_h - r_h) < 2), max(l_h, r_h) + 1
        
        return travel(root)[0]