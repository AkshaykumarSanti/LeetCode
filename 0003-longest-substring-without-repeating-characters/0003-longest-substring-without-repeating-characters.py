class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = ""
        maxi = 0
        for i in s:
            if i in r:
                idx = r.index(i)
                r = r[idx+1:]
            
            r = r + i
                
            maxi = max(maxi,len(r))
        return maxi