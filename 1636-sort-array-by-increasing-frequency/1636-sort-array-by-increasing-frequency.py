class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        key = sorted(h,key=lambda x : (h[x],-x))

        res = []
        for i in key:
            res.extend([i] * h[i])
        
        return res