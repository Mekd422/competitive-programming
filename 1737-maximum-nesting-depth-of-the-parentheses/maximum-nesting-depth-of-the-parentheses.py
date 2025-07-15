class Solution(object):
    def maxDepth(self, s):
        """
        max depth
        """
        stack = []
        maxi = 0
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                maxi = max(maxi, len(stack))
                stack.pop()
        return maxi        

        