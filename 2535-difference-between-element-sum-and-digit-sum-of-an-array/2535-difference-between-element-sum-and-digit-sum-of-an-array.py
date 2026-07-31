class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0 
        for i in nums:
            sum1 = sum1 + i

        sum2 = 0
        for i in nums:
            while i > 0:
                sum2 = sum2 + i % 10
                i = i // 10
        
        return sum1 - sum2

        

        