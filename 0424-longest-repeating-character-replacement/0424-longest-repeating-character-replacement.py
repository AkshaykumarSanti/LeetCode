class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = ""
        count = 0
        ans = 0
        h = {}

        for i in range(len(s)):
            a = a + s[i]

            if s[i] in h:
                h[s[i]] += 1
            else:
                h[s[i]] = 1
            
            count = max(count, h[s[i]])

            while len(a) - count > k:
                h[a[0]] -= 1
                a = a[1:]
            
            ans = max(ans, len(a))
        
        return ans