# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        while(head):
            head = head.next
            if(slow == head):
                return True
            slow = slow.next
            if(not head):
                return False
            head = head.next
        return False