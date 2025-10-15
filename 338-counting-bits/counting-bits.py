class Solution:
    def countBits(self, n: int) -> List[int]:

        ans =  [0]

        def decimal_to_binary(n):
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary
            
        

        for i in range(1, n + 1):
            res = decimal_to_binary(i)
            ans.append(res.count("1"))
        return ans


        