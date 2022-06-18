
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        
        while(fast):
            fast = fast.next
            if(fast == slow):
                return True
            if(not fast):
                return False
            slow = slow.next
            fast = fast.next
        
        return False