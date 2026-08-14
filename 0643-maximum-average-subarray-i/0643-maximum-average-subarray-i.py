class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        x = 0
        average = float('-inf')
        for j in range(len(nums)):
            x = x + nums[j]

            if j-i+1 == k:
                if  x/k > average:
                    average = x/k
            
                x = x - nums[i]
                i = i + 1
        
        return average






        

        