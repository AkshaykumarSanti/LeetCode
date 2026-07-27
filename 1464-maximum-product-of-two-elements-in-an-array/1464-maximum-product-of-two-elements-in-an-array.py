class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 1
        second = 1
        for i in nums:
            if i >= first:
                second = first
                first = i
            elif i > second and i < first:
                second = i

        return (first-1) * (second-1)
        