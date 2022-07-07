# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        def travel(r):
            if not r:
                return []
            
            return travel(r.left) + [r.val] + travel(r.right)
        self.l = travel(root)

    def next(self) -> int:
        self.idx += 1
        return self.l[self.idx - 1]
        

    def hasNext(self) -> bool:
        return self.idx < len(self.l)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()