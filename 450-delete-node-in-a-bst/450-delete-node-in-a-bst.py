# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        #key is in left of the root, delete in the left tree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        #key is in the right of the root, delete in the right tree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        #the root is to be deleted
        else:
            #case 1, no child
            if not root.left and not root.right:
                return None
            #case 2, one child
            elif not (root.left and root.right):
                #return whatever child that is not null
                return root.left if root.left else root.right
            #case 3, two children
            else:
                temp = root.right
                while(temp.left):
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
                
        return root
                
                
            