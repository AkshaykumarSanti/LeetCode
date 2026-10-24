class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def convert(date):
            month = int(date[:2])
            day = int(date[3:])

            total = day
            for i in range(month - 1):
                total += days[i]
            
            return total

        aa = convert(arriveAlice)
        al = convert(leaveAlice)
        ba = convert(arriveBob)
        bl = convert(leaveBob)

        start = max(aa,ba)
        end = min(al,bl)

        return max(0, end - start + 1)
