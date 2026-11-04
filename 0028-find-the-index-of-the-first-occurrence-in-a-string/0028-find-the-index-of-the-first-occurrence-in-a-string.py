class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
            
        length = 0
        for i in needle:
            length += 1
        
        for i in range(len(haystack) - length + 1):
            x = ""
            for j in range(i,i + length):
                x = x + haystack[j]
            
            if x == needle:
                return i
        
        return -1