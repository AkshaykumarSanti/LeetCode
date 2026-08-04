class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        i = nums[0]
        j = nums[-1]

        for i in range(i,j+1):
            if i not in nums:
                res.append(i)
        
        return res