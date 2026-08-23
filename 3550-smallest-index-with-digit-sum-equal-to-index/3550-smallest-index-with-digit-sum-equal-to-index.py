class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            if nums[i] < 10 and i == nums[i]:
                return i
            elif nums[i] >= 10:
                s = 0
                n = nums[i]
                while n != 0:
                    r = n % 10
                    n = n // 10
                    s = s + r
                if s == i:
                    return i
        
        return ans
        