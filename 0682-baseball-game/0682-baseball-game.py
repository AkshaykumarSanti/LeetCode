class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for i in ops:
            if i == "C" and len(s) > 0:
                s.pop()
            elif i == "D":
                s.append(s[-1] * 2)
            elif i == "+":
                s.append(s[-1] + s[-2])
            else:
                s.append(int(i))

        return sum(s)