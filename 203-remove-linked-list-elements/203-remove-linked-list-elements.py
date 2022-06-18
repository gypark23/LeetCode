# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while(head and head.val == val):
            head = head.next
        
        ret = head
        prev = None
        while(head):
            if(head.val == val):
                prev.next = head.next
            else:
                prev = head
            head = head.next
            
        return ret