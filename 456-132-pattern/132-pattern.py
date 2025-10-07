class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # if len(nums) < 3:
        #     return False
        
        # stack = []
        # for i in range(len(nums)):
        #     if len(stack) >= 2 and stack[len(stack) - 2] < nums[i] < stack[-1] :
        #         return True
        #     stack.append(nums[i])
        # return False
        stack = []
        third = float('-inf')

        for num in reversed(nums):
            if num < third:
                return True
            while stack and num > stack[-1]:
                third = stack.pop()
            stack.append(num)
        return False 
            
        