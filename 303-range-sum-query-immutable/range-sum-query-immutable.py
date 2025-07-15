class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        summ = 0
        for i in nums:
            summ += i
            self.prefix.append(summ)

        

    def sumRange(self, left, right):
        """
        sum range
        """
        rightS = self.prefix[right]
        leftS = self.prefix[left - 1] if left > 0 else 0
    
        return rightS - leftS

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)