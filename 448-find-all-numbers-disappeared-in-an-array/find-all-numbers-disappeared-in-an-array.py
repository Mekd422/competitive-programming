class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        find disappeared number
        """
        res = []
        i = 0
        while i < (len(nums)):
            
            correct_pos = nums[i] - 1
            if nums[correct_pos] != nums[i]:
                nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
            else:
                i += 1
              
        for i in range(len(nums) ):
            if nums[i] != i + 1:
                res.append(i + 1)
            else:
                continue    
        return res        

        