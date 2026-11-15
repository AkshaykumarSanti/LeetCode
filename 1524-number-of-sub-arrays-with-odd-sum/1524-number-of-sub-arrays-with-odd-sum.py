class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = 0
        even = 1
        res = 0
        total = 0

        for i in arr:
            total += i
            if total % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
        
        return res % (10 ** 9 + 7)