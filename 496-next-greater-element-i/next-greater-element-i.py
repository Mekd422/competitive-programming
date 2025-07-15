class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        next greater element
        """
        result = [-1] * len(nums2)
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                result[index] = nums2[i]
            stack.append(i)
        
        ans = []
        for number in nums1:
            idx = nums2.index(number)
            ans.append(result[idx])
        return ans