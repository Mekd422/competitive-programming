class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def helper(i, j):
            if i == j :
                return nums[i]

            left = nums[i] - helper(i + 1, j)
            right = nums[j] - helper(i, j - 1)

            return max(left, right)

        return (helper(0, len(nums) - 1)) >= 0

        
        