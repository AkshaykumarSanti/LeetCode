class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        first = sorted(s[:n // 2])

        if n % 2 == 0:
            return "".join(first + first[::-1])
        else:
            return "".join(first + [s[n//2]] + first[::-1])
        