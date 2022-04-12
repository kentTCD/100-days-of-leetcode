class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        order_list = []
        i = 0
        for row in mat:
            if i == 0:
                order_list.append(0)
            else:
                row_sum = sum(row)
                j = 0
                for row_index in order_list:
                    if row_sum < sum(mat[row_index]):
                        order_list.insert(j, i)
                        j = j + 1
                        break
                    if j == len(order_list) - 1:
                        order_list.append(i)
                        break
                    j = j + 1

            i = i + 1

        return order_list[0:k]