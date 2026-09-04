class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            h1 = {}
            h2 = {}
            mark = True
            for i in range(len(word)):
                if word[i] in h1 and h1[word[i]] != pattern[i]:
                    mark = False
                    break
                if pattern[i] in h2 and h2[pattern[i]] != word[i]:
                    mark = False
                    break

                h1[word[i]] = pattern[i]
                h2[pattern[i]] = word[i]

            if mark:
                result.append(word) 
        
        return result
