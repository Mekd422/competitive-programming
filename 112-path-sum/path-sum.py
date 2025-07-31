# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def path(node, curr_sum):
            if not node:
                return False

            curr_sum += node.val

            if not node.left and not node.right:
                return curr_sum == targetSum

            return path(node.left, curr_sum) or path(node.right, curr_sum)

        return path(root, 0)

        

        