# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self._count = 0
        
        def count(self, r):
            if(not r):
                return True
            
            if(not r.left and not r.right):
                self._count += 1
                return True
            
            left_bool, right_bool = True, True
            
            if(r.left):
                left_bool = count(self, r.left)
                if(left_bool):
                    if(r.val == r.left.val):
                        left_bool = True
                    else:
                        left_bool = False
            if(r.right):
                right_bool = count(self, r.right)
                if(right_bool):
                    if(r.val == r.right.val):
                        right_bool = True
                    else:
                        right_bool = False
            
            self._count += left_bool and right_bool
            return left_bool and right_bool
        
        count(self, root)
        return self._count
                