class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        h = {}

        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            
            if h[i] <= k:
                res.append(i)

        return res