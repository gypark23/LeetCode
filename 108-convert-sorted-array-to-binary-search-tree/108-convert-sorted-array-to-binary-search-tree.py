# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(low, high):
            if low > high:
                return None
            
            mid = (low + high) // 2
            ret = TreeNode(nums[mid])
            ret.left = build(low, mid - 1)
            ret.right = build(mid + 1, high)
            return ret
        
        return build(0, len(nums) - 1)
            