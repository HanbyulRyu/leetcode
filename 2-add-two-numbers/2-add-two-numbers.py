# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = result_node = ListNode()
        add_n = 0
        
        while l1 or l2 or add_n:
            #print("l1_value", l1.val, "l2_value", l2.val, "addNumber", addNumber)
            l1_value = 0
            l2_value = 0
            
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_value = l2.val
                l2 = l2.next
        
            sum_n = l1_value + l2_value + add_n
           
            result = sum_n % 10
            add_n = sum_n // 10

            temp_node.next = ListNode(result)
            temp_node = temp_node.next
            #print(resultNode)
        
        return result_node.next
                