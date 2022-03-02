# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next   
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lengthHead = head
        temp = head
        length = 0
        
        while lengthHead:
            length += 1
            lengthHead = lengthHead.next
        
        position = length - n
        
        if (length == 1 and n == 1) or position == 0:
            return head.next
        
        
        
        while position > 1:
            if temp.next:
                temp = temp.next
                position -= 1
            else: 
                return temp
            
        temp.next = temp.next.next
        
        return head
                    
