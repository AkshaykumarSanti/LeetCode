class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        k = 3
        for i in range(len(num) - k + 1):
            x = ""
            for j in range(i,i + k):
                x = x + num[j]
            res.append(x)

        maxi = ""
        for i in res:
            if i[0] == i[1] == i[2]:
                a = i[0] * 3
                if a > maxi:
                    maxi = a
        return maxi
