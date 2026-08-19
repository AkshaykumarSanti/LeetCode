class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        k = 0
        for i in range(len(s)):
            if k < len(spaces) and i == spaces[k]:
                res = res + " "
                k = k + 1
            
            res = res + s[i]
    
        return res

        