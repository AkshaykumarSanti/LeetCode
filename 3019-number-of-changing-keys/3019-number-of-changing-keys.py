class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        change = 0
        for i in range(len(s)-1):
            if s[i] != s[i + 1]:
                change += 1
        return change