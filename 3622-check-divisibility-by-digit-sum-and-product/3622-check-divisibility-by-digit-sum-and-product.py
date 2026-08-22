class Solution:
    def checkDivisibility(self, n: int) -> bool:
        copy = n
        s = 0
        p = 1
        while n != 0:
            r = n % 10
            n = n // 10
            s = s + r
            p = p * r
        
        ans = copy % (s + p) 

        if ans == 0:
            return True
        return False
        