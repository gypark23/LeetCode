# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        stack = []
        while(temp):
            stack.append(temp.val)
            temp = temp.next
        
        for i in range(len(stack)):
            if(i % 2 == 0):
                head.val = stack[i // 2]
            else:
                head.val = stack[-(i // 2 + 1)]
            head = head.next
        