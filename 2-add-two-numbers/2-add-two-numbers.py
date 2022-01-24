# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = resultNode = ListNode()
        resultArray = []
        addNumber = 0
        
        while l1 or l2 or addNumber:
            #print("l1_value", l1.val, "l2_value", l2.val, "addNumber", addNumber)
            l1_value = 0
            l2_value = 0
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_value = l2.val
                l2 = l2.next
        
            sumNumber = l1_value + l2_value + addNumber
           
            result = sumNumber % 10
            addNumber = sumNumber // 10

            tempNode.next = ListNode(result)
            tempNode = tempNode.next
            #print(resultNode)
        
        return resultNode.next
                