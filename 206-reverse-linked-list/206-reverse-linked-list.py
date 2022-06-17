# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """iterative
        curr = head
        prev = None
        
        while(curr):
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        
        return prev
        """
        """recursive"""
        
        def reverse(previous, curr):
            if(not curr):
                return previous
            
            next_temp = curr.next
            curr.next = previous
            return reverse(curr, next_temp)
        
        return reverse(None, head)