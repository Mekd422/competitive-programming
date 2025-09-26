class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for ch in s:
            if ch == "(":
                low += 1
                high += 1
            elif ch == ")":
                low = max(0, low - 1)
                high -= 1

            else:
                low = max(0, low - 1)
                high += 1

            if high < 0:
                return False
        return low == 0
        