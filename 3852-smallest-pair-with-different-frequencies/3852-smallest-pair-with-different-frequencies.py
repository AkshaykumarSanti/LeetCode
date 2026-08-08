class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        keys = sorted(h)

        for i in range(len(keys)):
            for j in range(i+1,len(keys)):
                if h[keys[i]] != h[keys[j]]:
                    return [keys[i],keys[j]]
        
        return [-1,-1]

         