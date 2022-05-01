class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        fin_point = coordinates[-1]
        for i in range(len(coordinates)-1):
            y_increase = fin_point[1] - coordinates[i][1]
            x_increase = fin_point[0] - coordinates[i][0]
            tmp_slope = y_increase / x_increase if y_increase != 0 and x_increase != 0 else 0
            if i == 0: slope = tmp_slope
            if slope != tmp_slope: return False
        return True