# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ''''''
        self.cnt = 0

        def dfs(node):
            if not node:
                return (0, 0)  

            left_sum, left_count = dfs(node.left)  
            right_sum, right_count = dfs(node.right) 

            total_sum = left_sum + right_sum + node.val  
            total_count = left_count + right_count + 1  

            if node.val == total_sum // total_count: 
                self.cnt += 1

            return (total_sum, total_count)

        dfs(root)
        return self.cnt

        
        
        