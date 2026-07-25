class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        res = [0] * len(nums)
        k = len(nums) - 1
        while i <= j:
            a = nums[i] * nums[i] 
            b = nums[j] * nums[j]
            if a < b:
                res[k] = b
                k = k - 1
                j = j - 1
            elif a >= b:
                res[k] = a
                k = k - 1
                i = i + 1
        return res 
        