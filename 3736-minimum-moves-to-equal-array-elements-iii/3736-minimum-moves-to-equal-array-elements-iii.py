class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        count = 0

        for num in nums:
            count += m - num
        
        return count