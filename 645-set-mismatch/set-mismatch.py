class Solution(object):
    def findErrorNums(self, nums):
        """
            find error nums
        """
        i = 0
        ans = []
        while i < len(nums):
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(nums[i])
                ans.append(i + 1)    
        return ans                
        