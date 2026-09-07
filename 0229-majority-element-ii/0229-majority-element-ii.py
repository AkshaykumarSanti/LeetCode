class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        h = {}
        for i in nums:
            if i in h:
                h[i] = h[i] + 1
            else:
                h[i] = 1

        res = []
        for i in h:
            if  h[i] > (n/3):
                res.append(i)

        return res