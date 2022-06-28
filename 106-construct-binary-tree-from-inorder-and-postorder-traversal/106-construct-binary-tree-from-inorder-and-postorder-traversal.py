# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.dic = {}
        for i, num in enumerate(inorder):
            self.dic[num] = i
        
        def helper(left, right):
            if(left > right):
                return None
            
            ret = TreeNode(postorder.pop())
            mid = self.dic[ret.val]
            
            ret.right = helper(mid + 1, right)
            ret.left = helper(left, mid - 1)
            
            return ret
        
        return helper(0, len(postorder) - 1)
            