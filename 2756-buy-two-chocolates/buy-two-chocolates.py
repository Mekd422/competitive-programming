class Solution(object):
    def buyChoco(self, prices, money):
        '''
            buy choco
        '''
        prices.sort()
        p = 0
        
        if prices[p] + prices[p + 1] <= money:
            ans = money - (prices[p] + prices[p + 1])
            return ans
        else:
            return money    
        
        
        