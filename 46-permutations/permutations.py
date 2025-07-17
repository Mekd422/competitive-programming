class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ''''''

        def permutation(list_of_candidates, path):
            if not list_of_candidates:  
                ans.append(path)
                return
            for i, num in enumerate(list_of_candidates):
                permutation(list_of_candidates[:i] + list_of_candidates[i+1:], path + [num])

        permutation(nums, []) 
        return ans

            


        