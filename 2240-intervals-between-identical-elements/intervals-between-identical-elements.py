class Solution(object):
    def getDistances(self, arr):
        """
        get distance
        """
        
        indx = defaultdict(list)
        
        n = len(arr)
      
       
        for i, num in enumerate(arr):
            indx[num].append(i)
          
       
        ans = [0] * n
      
        
        for indices in indx.values():
            
            m = len(indices)
            total_distance = sum(indices) - indices[0] * m
      
            for i, indx in enumerate(indices):
       
                delta = indices[i] - indices[i - 1] if i >= 1 else 0
               
                total_distance += i * delta - (m - i) * delta
                
                ans[indx] = total_distance
              
        return ans
        