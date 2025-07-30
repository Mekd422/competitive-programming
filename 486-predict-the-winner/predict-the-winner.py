class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def helper(i, j):
            if i == j :
                return nums[i]

            left = nums[i] - helper(i + 1, j)
            right = nums[j] - helper(i, j - 1)

            return max(left, right)

        return (helper(0, len(nums) - 1)) >= 0

        
        