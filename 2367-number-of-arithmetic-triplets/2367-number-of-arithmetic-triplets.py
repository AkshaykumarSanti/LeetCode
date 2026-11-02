class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0
        i = 0
        j = i + 1
        k = len(nums) - 1

        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
                    k = k + 1
                j = j + 1
            i = i + 1
        
        return count