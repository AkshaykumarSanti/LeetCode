class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()
        mini = float('inf')
        for i in range(len(nums)-k+1):
            s = nums[i:i+k]
            
            diff = s[-1] - s[0]
            
            if diff < mini:
                mini = diff
        
        return mini     