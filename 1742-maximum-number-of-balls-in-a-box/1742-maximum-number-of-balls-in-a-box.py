class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        h = {}

        for num in range(lowLimit, highLimit + 1):
            a = 0
        
            while num > 0:
                r = num % 10
                num = num // 10
                a += r
            
            if a in h:
                h[a] += 1
            else:
                h[a] = 1
        
        return max(h.values())