class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ['a','e','i','o','u']
        ans = 0
        count = 0

        for i in range(k):
            if s[i] in v:
                count += 1
        ans = count

        for i in range(k,len(s)):
            if s[i] in v:
                count += 1
            if s[i-k] in v:
                count -= 1
            if count > ans:
                ans = count

        return ans   