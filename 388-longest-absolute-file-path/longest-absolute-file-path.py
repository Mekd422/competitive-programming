class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_so_far = 0
        chunks = input.split("\n")
        paths = {}

        for char in chunks:
            level = 0
            while level < len(char) and char[level] == "\t":
                level += 1
            path_len = len(char) if level == 0 else paths[level - 1] + 1 + len(char[level:])

            if "." in char:
                max_so_far = max(max_so_far, path_len)

            else:
                paths[level] = path_len

        return max_so_far


        