class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length = 0
        for sentence in sentences:
            a = sentence.split()
            if len(a) > length:
                length = len(a)

        return length

        