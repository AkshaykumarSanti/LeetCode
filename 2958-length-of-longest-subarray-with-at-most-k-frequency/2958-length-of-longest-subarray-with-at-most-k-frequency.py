class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        h = {}
        i = 0
        maxi = 0

        for j in range(len(nums)):
            if nums[j] in h:
                h[nums[j]] += 1
            else:
                h[nums[j]] = 1

            while h[nums[j]] > k:
                h[nums[i]] -= 1
                i += 1

            count = j - i + 1

            if count > maxi:
                maxi = count

        return maxi