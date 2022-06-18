# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """hash table
        dic = {}
        
        while(headA):
            dic[headA] = 1
            headA = headA.next
        while(headB):
            if(headB in dic):
                return headB
            headB = headB.next
        
        return None
        """
        
        """two pointer"""
        
        lenA, lenB = 0, 0
        tempA, tempB = headA, headB
        while(tempA):
            lenA += 1
            tempA = tempA.next
        while(tempB):
            lenB += 1
            tempB = tempB.next
        
        long, short = headA if lenA >= lenB else headB, headB if lenA >= lenB else headA
        
        for i in range(abs(lenA - lenB)):
            long = long.next
        
        while(long and short):
            if(long == short):
                return long
            long = long.next
            short = short.next
        
        return None