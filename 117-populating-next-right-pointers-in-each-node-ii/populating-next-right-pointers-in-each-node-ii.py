"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        leftmost = root
        while leftmost:
            curr = leftmost
            prev = None
            leftmost = None

            while curr:
                for child in (curr.left, curr.right):
                    if child:
                        if prev:
                            prev.next = child
                        else:
                            leftmost = child
                        prev = child
                curr = curr.next
        return root
        