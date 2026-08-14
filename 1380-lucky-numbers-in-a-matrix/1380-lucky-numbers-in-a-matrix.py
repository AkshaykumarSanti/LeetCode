class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        col = []
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(columns):
            x = []
            for j in range(rows):
                a = matrix[j][i]
                x.append(a)
            col.append(x)

        res = []
        for i in range(rows):
            minimum = min(matrix[i])
            idx = matrix[i].index(minimum)

            if minimum == max(col[idx]):
                res.append(minimum)
        
        return res