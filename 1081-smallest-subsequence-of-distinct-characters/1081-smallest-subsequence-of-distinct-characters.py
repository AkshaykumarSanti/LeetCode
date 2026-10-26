class Solution:
    def smallestSubsequence(self, s: str) -> str:
        h = {}
        a = set()
        stack = []

        for i in range(len(s)):
            h[s[i]] = i

        for i in range(len(s)):
            ch = s[i]

            if ch in a:
                continue
            
            while stack and ch < stack[-1] and h[stack[-1]] > i:
                a.remove(stack.pop())
            
            a.add(ch)
            stack.append(ch)
        
        return "".join(stack)