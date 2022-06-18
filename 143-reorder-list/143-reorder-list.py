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
        #find midpoint
        mid, fast = head, head.next
        while(fast and fast.next):
            mid = mid.next
            fast = fast.next.next
        #reverse second half
        curr = mid.next
        prev = mid.next = None
        _next = None
        while(curr):
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        mid = prev
        
        #merge
        while(mid):
            head_next, mid_next = head.next, mid.next
            head.next = mid
            mid.next = head_next
            head, mid = head_next, mid_next
        

        """stack
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
       """ 