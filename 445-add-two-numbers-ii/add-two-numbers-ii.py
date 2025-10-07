# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        total = str(int(num1) + int(num2))
        dummy = ListNode(0)
        current = dummy
        for digit in total:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
            
        
        

        
        