# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        self.fillLeft(root)

    def fillLeft(self, r):
        while r:
            self.l.append(r)
            r = r.left
        
        
    def next(self) -> int:
        ret = self.l.pop()
        self.fillLeft(ret.right)
        return ret.val
    
    def hasNext(self) -> bool:
        return len(self.l) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()