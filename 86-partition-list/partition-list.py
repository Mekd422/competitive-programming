# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right =  ListNode(), ListNode()
        lleft, rright = left, right

        while head:
            if head.val < x:
                lleft.next = head
                lleft = lleft.next
            else:
                rright.next = head
                rright = rright.next
            head = head.next
        lleft.next = right.next
        rright.next = None
        return left.next
        