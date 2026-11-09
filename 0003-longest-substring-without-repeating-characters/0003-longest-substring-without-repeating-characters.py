class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = ""
        longest = 0

        for i in s:
            if i in r:
                idx = r.index(i)
                r = r[idx + 1:]
            
            r = r + i
        
            longest = max(longest, len(r))
        
        return longest