class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        memo = {}
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                return nums[i]

            pick_left = nums[i] - helper(i + 1, j)
            pick_right = nums[j] - helper(i, j -1)

            res =  max(pick_left, pick_right)
            memo[(i, j)] = res
            return res

        return helper(0, len(nums)  - 1) >= 0

        