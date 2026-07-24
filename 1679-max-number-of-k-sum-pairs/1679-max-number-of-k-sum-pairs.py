class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                count = count + 1
                i = i + 1
                j = j - 1
            elif s < k:
                i = i + 1
            else:
                j = j - 1

        return count