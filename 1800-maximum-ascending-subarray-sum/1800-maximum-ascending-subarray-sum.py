class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = 0
        sum = 0
        for i in range(len(nums)-1):
            sum += nums[i]

            if nums[i] >= nums[i+1]:
                if sum > maxi:
                    maxi = sum
                sum = 0

        sum += nums[-1]
        if sum > maxi:
            maxi = sum
        
        return maxi