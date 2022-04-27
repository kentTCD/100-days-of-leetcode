class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        ave = sum(salary[1:-1]) / (len(salary)-2)
        return ave