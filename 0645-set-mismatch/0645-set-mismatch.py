class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        for i in range(1,len(nums)+1):
            if i not in nums:
                res[1] = i
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        for i in h:
            if h[i] == 2:
                res[0] = i
        
        return res
        