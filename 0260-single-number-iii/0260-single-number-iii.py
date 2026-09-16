class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        res = []
        for i in h:
            if h[i] == 1:
                res.append(i)
        
        return res