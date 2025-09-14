class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def valid_part(s: str) -> bool:
            return not (len(s) > 1 and s[0] == '0')
        
       
        for i in range(1, n):            
            for j in range(i+1, n+1):    
                a_s = num[0:i]
                b_s = num[i:j]
                if not valid_part(a_s) or not valid_part(b_s):
                    continue
                a = int(a_s)
                b = int(b_s)
                k = j
                count = 2
               
                while k < n:
                    s = a + b
                    s_s = str(s)
                    # next part of string must match s_s
                    if not num.startswith(s_s, k):
                        break
                    # move window
                    k += len(s_s)
                    a, b = b, s
                    count += 1
                # if we consumed whole string and have at least 3 numbers -> success
                if k == n and count >= 3:
                    return True
        return False
            