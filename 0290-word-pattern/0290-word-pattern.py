class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        word = s.split()

        if len(pattern) != len(word):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] in h and h[pattern[i]] != word[i]:
                return False
            elif pattern[i] not in h and word[i] in h.values():
                return False
            else:
                h[pattern[i]] = word[i]

        return True