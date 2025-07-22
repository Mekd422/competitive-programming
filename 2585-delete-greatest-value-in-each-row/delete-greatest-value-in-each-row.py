
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        ''''''

        ans = 0
        for row in grid:
            row.sort()

        R = len(grid)
        C = len(grid[0])

        for i in range(C):
            max_num = grid[0][i]

            for j in range(R):
                max_num = max(max_num, grid[j][i])
            ans += max_num
        return ans 

            
        