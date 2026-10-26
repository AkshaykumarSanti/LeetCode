class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        a = 0

        for i in s:
            if i == "R":
                a = a + 1
            else:
                a = a - 1
            
            if a == 0:
                count = count + 1
        
        return count