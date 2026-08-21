class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        h = {}
        for i in chars:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        res = 0

        for word in words:
            s = {}
            for i in word:
                if i in s:
                    s[i] += 1
                else:
                    s[i] = 1

            mark = 0
            for i in s:
                if i not in h or s[i] > h[i]:
                    mark = 1
                    break
            
            if mark == 0:
                res = res + len(word)
        
        return res