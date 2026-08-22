class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avg = 0
        count = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                avg += i
                count += 1
        if count != 0:
            return int(avg/count)
        
        return 0