class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_num = max(nums)
        
        points = [0] * (max_num + 1)
        for num in count:
            points[num] = num * count[num]
        
        
        dp = [0] * (max_num + 1)
        dp[0] = 0
        dp[1] = points[1]
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
        
        return dp[max_num]
        