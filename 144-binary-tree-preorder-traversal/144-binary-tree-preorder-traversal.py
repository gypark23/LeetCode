# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """recursive
        def travel(r, _list):
            if(not r):
                return _list
            
            _list.append(r.val)
            travel(r.left, _list)
            travel(r.right, _list)
        
        ret = []
        travel(root, ret)
        return ret
        """
        """iterative"""
        
        ret = []
        stack = []
        
        if(root):
            stack.append(root)
        
        while(stack):
            temp = stack.pop()
            ret.append(temp.val)
            if(temp.right):
                stack.append(temp.right)
            if(temp.left):
                stack.append(temp.left)
            
        
        return ret
            