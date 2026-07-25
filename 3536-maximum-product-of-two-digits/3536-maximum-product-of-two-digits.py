class Solution:
    def maxProduct(self, n: int) -> int:
        if n < 10:
            return n
        a = -1
        b = -1
        while n != 0:
            r = n % 10
            n = n // 10
            if r > a:
                b = a
                a = r
            elif r > b:
                b = r
        return a * b
        
        