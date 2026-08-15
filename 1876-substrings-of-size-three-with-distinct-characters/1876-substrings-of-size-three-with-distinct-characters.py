class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sub = []
        for i in range(len(s)-3+1):
            a = s[i:i+3]

            sub.append(a)

        count = 0
        for k in sub:
            if k[0] != k[1] and k[1] != k[2] and k[0] != k[2]:
                count += 1
            
        return count

        