"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        def dfs(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance
            for sub in emp.subordinates:
                total += dfs(sub)
            return total
        
        return dfs(id)
        