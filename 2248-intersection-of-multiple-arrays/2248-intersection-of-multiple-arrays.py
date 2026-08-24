class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        h = {}
        for num in nums:
            for i in num:
                if i in h:
                    h[i] += 1
                else:
                    h[i] = 1
        
        res = []
        for i in h:
            if h[i] == len(nums):
                res.append(i)

        return sorted(res)