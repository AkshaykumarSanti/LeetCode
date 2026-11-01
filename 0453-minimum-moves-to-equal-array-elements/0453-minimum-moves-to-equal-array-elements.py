class Solution:
    def minMoves(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        
        mini = min(nums)
        count = 0

        for i in nums:
            count = count + (i - mini)
        
        return count