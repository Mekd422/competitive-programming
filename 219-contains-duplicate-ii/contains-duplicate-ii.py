class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        contains nerby duplicates
        """
        res = set()
    
        for i in range(len(nums)):
            if nums[i] in res:
                return True
            res.add(nums[i])
            if len(res) > k:
                res.remove(nums[i - k])
    
        return False       

    
    