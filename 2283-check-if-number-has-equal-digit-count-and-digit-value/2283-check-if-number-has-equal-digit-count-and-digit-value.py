class Solution:
    def digitCount(self, num: str) -> bool:
        h = {}
        for i in num:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        for i in range(len(num)):
            if int(num[i]) != h.get(str(i), 0):
                return False
        
        return True
