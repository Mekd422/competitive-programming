"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size) -> 'Node':
            if size == 1:
               
                return Node(val=grid[r][c] == 1, isLeaf=True)
            
            newSize = size // 2
            topLeft = build(r, c, newSize)
            topRight = build(r, c + newSize, newSize)
            bottomLeft = build(r + newSize, c, newSize)
            bottomRight = build(r + newSize, c + newSize, newSize)
            
           
            if (topLeft.isLeaf and topRight.isLeaf and 
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(val=topLeft.val, isLeaf=True)
            
           
            return Node(val=True, isLeaf=False, 
                        topLeft=topLeft, topRight=topRight,
                        bottomLeft=bottomLeft, bottomRight=bottomRight)
        
        n = len(grid)
        return build(0, 0, n)
        