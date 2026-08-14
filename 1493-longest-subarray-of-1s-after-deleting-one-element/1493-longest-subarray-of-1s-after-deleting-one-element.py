class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        zero = 0
        maxi = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero += 1

            while zero > 1:
                if nums[i] == 0:
                    zero -= 1
                i = i + 1
            
            maxi = max(maxi,j-i)
                
        return maxi