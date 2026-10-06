class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        h = {}

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1

        for i in h:
            if h[i] > 1:
                return i