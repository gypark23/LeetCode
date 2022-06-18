# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        prev = None
        carry = 0
        while(l1 and l2):
            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        
        
        if(l2):
            prev.next = l2
            l1 = l2
        
        while(l1):
            l1.val += carry
            carry = l1.val // 10
            l1.val %= 10
            prev = l1
            l1 = l1.next
        
        if(carry):
            last = ListNode()
            last.val = 1
            last.next = None
            prev.next = last
        
        return l1_head
        #print(l2_head)
        