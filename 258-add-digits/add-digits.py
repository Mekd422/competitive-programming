class Solution(object):
    def addDigits(self, num):
        """
        add digits
        """
        while num >= 10:
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            num = sum_digits 
        return num       
            