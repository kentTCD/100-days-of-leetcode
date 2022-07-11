class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(1, rowIndex+1):
            row = []
            prev_row = res[i-1]
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(prev_row[j-1] + prev_row[j])
            res.append(row)
        return res[rowIndex]