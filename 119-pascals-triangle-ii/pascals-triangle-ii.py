class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        # Recursive call to get previous row
        prev_row = self.getRow(rowIndex - 1)
        
        # Build current row by adding adjacent elements of previous row
        current_row = [1]  # first element is always 1
        
        for i in range(1, len(prev_row)):
            current_row.append(prev_row[i - 1] + prev_row[i])
            
        current_row.append(1)  # last element is always 1
        
        return current_row