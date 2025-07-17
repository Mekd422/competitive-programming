class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ''''''
        l, h = max(weights), sum(weights)
        ans = sum(weights)
        def validator(mid):
            weight_sofar = 0
            curr_days = 1
            for i in range(len(weights)):           
                weight_sofar += weights[i]
                if weight_sofar > mid:
                    curr_days += 1
                    weight_sofar = weights[i]
                    if curr_days > days:
                        return False
            return True
        while l <= h:
            mid = (l + h)//2          
            i = 0
            if validator(mid) == True:
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans



        