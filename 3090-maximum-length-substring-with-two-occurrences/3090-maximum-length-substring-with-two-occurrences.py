class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        h = {}
        j = 0
        maxi = 0

        for i in range(len(s)):
            if s[i] in h:
                h[s[i]] += 1
            else:
                h[s[i]] = 1

            while h[s[i]] > 2:
                h[s[j]] -= 1
                j = j + 1

            maxi = max(maxi,i-j+1)
        
        return maxi
        
        