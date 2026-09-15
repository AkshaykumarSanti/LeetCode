class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k == 1:
            return s
        
        ans = ""
        for i in range(0,len(s),1):
            if i == k-1:
                ans = s[:k][::-1] + s[k:]

        return ans