# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def travel(r):
            if(not r):
                return ""
            
            return ";" + str(r.val) + "_" + travel(r.left) + "-" + travel(r.right) + "."
        
        str1 = travel(root)
        str2 = travel(subRoot)
        print(str1, str2)
        
        return True if str1.find(str2) != -1 else False
            