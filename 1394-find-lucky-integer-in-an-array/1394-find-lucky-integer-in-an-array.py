class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h = {}
        for i in arr:
            if i in h:
                h[i] = h[i] + 1
            else:
                h[i] = 1
        res = -1
        for i in h:
            if h[i] == i:
                if i > res:
                    res = i
        return res

        