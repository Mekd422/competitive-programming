class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        prev_row = self.getRow(rowIndex - 1)
        curr_row = [1]

        for i in range(1, len(prev_row)):
            curr_row.append(prev_row[i - 1] + prev_row[i])

        curr_row.append(1)

        return curr_row
    
        

        