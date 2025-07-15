class Solution(object):
    def isPowerOfTwo(self, n):
        '''
        power of two
        '''
        x = 0
        while x <= 31:
            if ((2) ** x) == n :
                return True
            x += 1
        return False
                   


        
        