# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return None
        
        odd_first, even_first = head, head.next
        odd, even = head, head.next
        
        while(even and even.next):
            even = odd.next
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = even_first
        
        return head
            
        