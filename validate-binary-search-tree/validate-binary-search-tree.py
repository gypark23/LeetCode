# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def travel(r, low, high):
            if not r:
                return True
            
            return r.val > low and r.val < high and travel(r.left, low, r.val) and travel(r.right, r.val, high)
        
        return travel(root, -(2 ** 31 + 1), (2**31))