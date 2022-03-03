# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, start = None, None
        
        # 둘 다 빈 리스트일 경우 None, 하나만 빈 리스트 일경우 다른 하나를 return
        if not l1 and not l2:
            return head
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        # 둘 중 첫 값이 작은 값을 start 값에 셋팅
        if l1.val < l2.val:
            start = l1
            l1 = l1.next
        else :
            start = l2
            l2 = l2.next

        head = start

        # 작은 값을 넣어주도록 한다.
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
                
        # 남아있는 값을 뒤에 붙여준다.
        if l1:
            start.next = l1
        
        if l2:
            start.next = l2
            
        return head