# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, start = None, None
        
        
        if not l1 and not l2:
            return head
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        if l1.val < l2.val:
            start = l1
            l1 = l1.next
        else :
            start = l2
            l2 = l2.next

        head = start
        
        while l1 and l2:
            next = None
            l1_v = l1.val
            l2_v = l2.val
            
            if l1_v < l2_v:
                next = l1
                l1 = l1.next
            else:
                next = l2
                l2 = l2.next

            start.next = next
            start = start.next
                
        if l1:
            start.next = l1
        
        if l2:
            start.next = l2
            
        print(head)
        return head