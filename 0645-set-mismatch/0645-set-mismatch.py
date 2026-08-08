class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        h= {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        d = 0
        m = 0

        for i in range(1,len(nums)+1):
            if i not in h:
                m = i
            elif h[i] == 2:
                d = i
        
        return [d,m]
        