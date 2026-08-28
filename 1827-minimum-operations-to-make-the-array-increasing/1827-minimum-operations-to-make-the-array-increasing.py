class Solution:
    def minOperations(self, nums: List[int]) -> int:
        oper = 0
        for i in range(len(nums)-1):
            s = 0
            if nums[i] < nums[i+1]:
                pass
            else:
                s = (nums[i]-nums[i+1]+1)
                nums[i+1] = s + nums[i+1]
            
            oper += s
        
        return oper