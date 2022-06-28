# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.dic = {num : i for i,num in enumerate(inorder)}
        
        def helper(left, right):
            if(left > right):
                return None
            
            ret = TreeNode(preorder.pop(0))
            mid = self.dic[ret.val]
            
            ret.left = helper(left, mid - 1)
            ret.right = helper(mid + 1, right)
            
            return ret
        
        return helper(0, len(preorder) - 1)
            