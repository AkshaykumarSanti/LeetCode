class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)
        for word in words:
            word = set(word)
            if word.issubset(allowed):
                count += 1

        return count