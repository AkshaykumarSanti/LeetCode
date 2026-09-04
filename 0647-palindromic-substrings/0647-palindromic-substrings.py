class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            x = ""
            for j in range(i,len(s)):
                x = x + s[j]
                if x == x[::-1]:
                    count += 1
        return count