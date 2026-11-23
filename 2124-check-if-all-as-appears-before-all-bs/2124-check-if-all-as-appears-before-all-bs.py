class Solution:
    def checkString(self, s: str) -> bool:
        ans = 0
        for i in s:
            if i == 'b':
                ans = 1
            elif i == 'a' and ans == 1:
                return False
        else:
            return True