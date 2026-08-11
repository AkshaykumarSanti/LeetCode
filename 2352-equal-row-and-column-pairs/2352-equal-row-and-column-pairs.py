class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        h = {}
        for i in grid:
            temp = str(i)
            if temp in h:
                h[temp] += 1
            else:
                h[temp] = 1

        res = []
        for i in range(len(grid)):
            a = []
            for j in range(len(grid)):
                a.append(grid[j][i])
            
            res.append(a)

        s = {}
        for i in res:
            temp = str(i)
            if temp in s:
                s[temp] += 1
            else:
                s[temp] = 1

        count = 0
        for i in h:
            if i in s:
                count += h[i] * s[i]
        
        return count