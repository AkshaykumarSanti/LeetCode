class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i] <= s[i+1] for i in range(len(s) - 1)):
            return 0
        
        if len(s) == 2:
            return -1

        maxi = max(s)
        mini = min(s)

        if s[0] == mini or s[-1] == maxi:
            return 1
        
        for i in range(1,len(s)-1):
            if s[i] == mini or s[i] == maxi:
                return 2
        
        return 3