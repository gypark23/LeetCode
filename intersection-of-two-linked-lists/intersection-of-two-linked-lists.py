# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        headA_cpy, headB_cpy = headA, headB
        while(headA_cpy):
            lenA += 1
            headA_cpy = headA_cpy.next
        while(headB_cpy):
            lenB += 1
            headB_cpy = headB_cpy.next
        
        long, short = headA if lenA >= lenB else headB, headA if lenA < lenB else headB
        
        for i in range(abs(lenA - lenB)):
            long = long.next
        
        while(long):
            if(long == short):
                return long
            long = long.next
            short = short.next
        
        
        return None
        
            