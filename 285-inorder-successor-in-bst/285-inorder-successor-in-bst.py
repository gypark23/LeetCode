# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        l = []
        
        def travel(r):
            if not r:
                return []
            return travel(r.left) + [r] + travel(r.right)
        
        l = travel(root)
        idx = l.index(p)
        return l[idx + 1] if idx is not len(l) - 1 else None