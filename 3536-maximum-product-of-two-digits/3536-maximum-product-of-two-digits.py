class Solution:
    def maxProduct(self, n: int) -> int:
        res = []
        while n != 0:
            r = n % 10
            n = n // 10
            res.append(r)
        a = []
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                s = res[i] * res[j]
                a.append(s)

        return max(a)
        