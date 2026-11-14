class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float("Inf")

        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                k = j - i + 1

                if sum > 0 and k >= l and k <= r:
                    ans = min(ans, sum)
        
        if ans == float("Inf"):
            return -1
        
        return ans