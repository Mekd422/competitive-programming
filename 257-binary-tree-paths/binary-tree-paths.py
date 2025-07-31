# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def path(node, curr_path):
            if not node:
                return

            curr_path += str(node.val)

            if not node.left and not node.right:
                ans.append(curr_path)
                return
            curr_path += "->"

            path(node.left, curr_path)
            path(node.right, curr_path)

        path(root, "")
        return ans
            
        