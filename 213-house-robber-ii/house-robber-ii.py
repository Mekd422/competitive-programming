class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1 = rob2 = 0

        for i in range(len(nums) - 1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        ans1 = rob2

        ro1 = ro2 = 0

        for i in range(1, len(nums)):
            temp = max(nums[i] + ro1, ro2)
            ro1 = ro2
            ro2 = temp
        ans2 = ro2

        return max(ans1,  ans2)
        