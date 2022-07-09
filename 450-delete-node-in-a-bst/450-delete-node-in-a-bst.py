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
                root = None
            #case 3, has two children
            elif root.left and root.right:
                #find leftest in root.right
                temp_pre = root
                temp = root.right
                while(temp.left):
                    temp_pre = temp
                    temp = temp.left
                #if temp has a child (temp.right), link that to temp_pre.right or left
                if(temp.right):
                    if(temp.right.val < temp_pre.val):
                        temp_pre.left = temp.right
                    else:
                        temp_pre.right = temp.right
                #put temp to root
                root.val = temp.val
                root.left = self.deleteNode(root.left, root.val)
                root.right = self.deleteNode(root.right, root.val)
            #case 2, has one child
            else:
                root = root.left if root.left else root.right
        
        return root
                
                
            