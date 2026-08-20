class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            c = max(a,b+nums[i])

            b = a
            a = c
        
        return a