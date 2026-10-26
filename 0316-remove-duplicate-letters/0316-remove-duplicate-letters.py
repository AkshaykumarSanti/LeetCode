class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        h = {}
        stack = []

        for i in range(len(s)):
            h[s[i]] = i

        a = set()
        for i in range(len(s)):
            ch = s[i]

            if ch in a:
                continue
            
            while stack and ch < stack[-1] and h[stack[-1]] > i:
                a.remove(stack.pop())
            
            stack.append(ch)
            a.add(ch)
        
        return "".join(stack)