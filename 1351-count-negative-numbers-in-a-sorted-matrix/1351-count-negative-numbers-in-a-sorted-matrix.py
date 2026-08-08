class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negetive = 0
        for matrix in grid:
            for i in matrix:
                if i < 0:
                    negetive += 1
        return negetive

        