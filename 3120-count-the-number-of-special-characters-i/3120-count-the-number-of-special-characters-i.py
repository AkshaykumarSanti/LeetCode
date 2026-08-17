class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        word = set(word)
        for i in word:
            if chr(ord(i)-32) in word:
                count += 1
        
        return count

        