class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = Counter(s)
        stack = []

        for char in s:
            d[char] -= 1
            if char in stack:
                continue
            while stack and d[stack[-1]] > 0 and stack[-1] > char:
                stack.pop()
            stack.append(char)

        return "".join(stack)
        