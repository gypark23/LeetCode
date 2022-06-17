# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        while(head.next):
            head = head.next
            slow = slow.next
            if(not head.next):
                return slow
            head = head.next
        
        return slow