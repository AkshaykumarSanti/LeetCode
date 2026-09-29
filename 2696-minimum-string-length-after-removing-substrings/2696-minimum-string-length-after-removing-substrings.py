class Solution:
    def minLength(self, s: str) -> int:
        ans = []

        for i in s:
            if len(ans) > 0 and (i == "B" and ans[-1] == "A" or i == "D" and ans[-1] == "C"):
                ans.pop()
            else:
                ans.append(i)

        return len(ans)