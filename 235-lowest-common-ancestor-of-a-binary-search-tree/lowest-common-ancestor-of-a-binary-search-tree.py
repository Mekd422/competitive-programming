# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root:
        #     return 

        # if root == p or root == q:
        #     return root
        # if root.left == p and root.right == q or root.left == q and root.right == p:
        #     return root
        # if root.left == p and root != q:
        #     return root.left
        # if root.left == q or root != q:
        #     return root.right

        # return self.lowestCommonAncestor(root.left)
        # return self.lowestCommonAncestor(root.right)

        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr


        