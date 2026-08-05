class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        length = 0
        a = 0
        for i in s:
            if i == letter:
                a += 1
                length += 1
            else:
                length += 1
        
        return int((a/length) * 100)
        


        