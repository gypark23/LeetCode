# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid, fast = head, head.next
        
        while(fast and fast.next):
            fast = fast.next.next
            mid = mid.next
        
        prev = mid
        mid = mid.next
        prev.next = None
        
        prev = None
        curr = mid

        while(curr):
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        
        while(prev):
            if(head.val != prev.val):
                return False
            head = head.next
            prev = prev.next
        
        return True