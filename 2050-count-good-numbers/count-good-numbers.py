class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7 

        def pow(x, n):
            if n == 0:
                return 1

            half = pow(x, n // 2)
            if n % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * x) % MOD

        even = ceil(n / 2)
        odd = n // 2

        return (pow(5, even) * pow(4, odd)) % MOD