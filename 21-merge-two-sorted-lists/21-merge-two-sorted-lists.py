# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def build(r, l1, l2):
            if not l1 or not l2:
                r.next = l1 if l1 else l2
                return
            else:
                if l1.val < l2.val:
                    r.next = l1
                    l1 = l1.next
                else:
                    r.next = l2
                    l2 = l2.next
                build(r.next, l1, l2)
        
        ret = ListNode()
        build(ret, list1, list2)
        return ret.next