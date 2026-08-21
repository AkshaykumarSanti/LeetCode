class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        h = {}
        for i in nums:
            if i in h:
                count = count + h[i]
                h[i] = h[i] + 1
            else:
                h[i] = 1
        
        return count