class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr,num))
                curr = ""
                num = 0
            elif ch == "]":
                prev, times = stack.pop()
                curr = prev + curr * times
            else:
                curr += ch

        return curr