class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        total1 = 0
        psum = []

        for i in range(1,n+1):
            total1 += i
            psum.append(total1)

        total2 = 0
        for i in range(n,0,-1):
            total2 += i
            if total2 in psum:
                index = psum.index(total2) + 1
                if index == i:
                    return i

        return -1