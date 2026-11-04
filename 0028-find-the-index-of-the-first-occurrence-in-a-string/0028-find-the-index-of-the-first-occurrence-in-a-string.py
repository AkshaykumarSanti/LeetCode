class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = 0
        for i in needle:
            length += 1
        
        sub = []
        for i in range(len(haystack) - length + 1):
            x = ""
            for j in range(i,i + length):
                x = x + haystack[j]
            
            sub.append(x)
        
        for i in range(len(sub)):
            if sub[i] == needle:
                return i
        
        return -1