class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        stack = [0]
        visited = set()

        while stack:
            i = stack.pop()
            if i == len(s):
                return True
            if i in visited:
                continue
            visited.add(i)

            for j in range(i+1,len(s)+1):
                if s[i:j] in words:
                    stack.append(j)

        return False     