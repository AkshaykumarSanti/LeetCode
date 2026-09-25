class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            a = []
            for i in res:
                a.append(i + [num])
            res.extend(a)

        return res