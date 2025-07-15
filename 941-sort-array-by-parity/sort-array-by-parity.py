class Solution(object):
    def sortArrayByParity(self, nums):
        """
        sort array by parity
        """
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[r] % 2 == 0 and nums[l] % 2 != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1
            elif nums[r] % 2 != 0:
                r -= 1
            elif nums[r] % 2 == 0 and nums[l] % 2 == 0:
                l += 1
               
        return nums            


        