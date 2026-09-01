class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        k = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                ans[k] = 1
                k = k - 1
        
        return ans       