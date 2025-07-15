class Solution(object):
    def findMaxLength(self, nums):
        """
        find max length
        
        """
        max_length = 0
        
        cnt = 0
        cnt_map = {0: -1}  
    
        for i in range(len(nums)):
        
            if nums[i] == 0:
                cnt -= 1
            else:
                cnt += 1
        
            if cnt in cnt_map:
            
                max_length = max(max_length, i - cnt_map[cnt])
            else:
            
                cnt_map[cnt] = i
    
        return max_length       



        