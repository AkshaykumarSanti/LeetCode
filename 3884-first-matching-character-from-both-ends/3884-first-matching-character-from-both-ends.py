class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        count = -1
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                count = i
                break
            else:
                i = i + 1
                j = j - 1
        
        return count