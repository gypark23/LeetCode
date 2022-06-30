# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        queue = deque()
        ret = []
        if(root):
            queue.append(root)
        
        while(queue):
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if(curr):
                    ret.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    ret.append(None)
        
        return (str(ret)[1:-1])
            

    def deserialize(self, data):
        numlist = data.split(", ")
        if(len(data) == 0):
            return None
        
        head = TreeNode(numlist[0])
        numlist.pop(0)
        queue = [head]
        while(numlist):
            curr = queue.pop(0)
            l, r = numlist.pop(0), numlist.pop(0)
            if(l != "None"):
                l = TreeNode(int(l))
                queue.append(l)
            else:
                l = None
            if(r != "None"):
                r = TreeNode(int(r))
                queue.append(r)
            else:
                r = None
            curr.left = l
            curr.right = r

        return head
        
            
        
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))