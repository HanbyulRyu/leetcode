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
        
        # head의 길이 [1,2,3,4,5] = 5
        while lengthHead:
            length += 1
            lengthHead = lengthHead.next
        
        # 지우고 싶은 위치 5 - 2 = 3
        position = length - n
              
        # head 길이가 1이면서 첫번째 노드를 지우고 싶은 경우
        if length == 1 and n == 1:
            return head.next
        
        # 마지막 노드를 지우고 싶은 경우
        if position == 0:
            return head.next
        
        # 원하는 위치의 앞까지 이동해야하기 때문에 > 1 까지만 [3,4,5]
        while position > 1:
            if temp.next:
                temp = temp.next
                position -= 1
        # temp = [3, 5], head = [1,2,3,5]
        temp.next = temp.next.next
        return head
                    
