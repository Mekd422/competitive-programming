# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        def findMiddle(head):
            slow =  fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow

        if not head.next:
            return TreeNode(head.val)

        mid = findMiddle(head)
        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head if head != mid else None)
        root.right = self.sortedListToBST(mid.next)

        return root 
        


            
        