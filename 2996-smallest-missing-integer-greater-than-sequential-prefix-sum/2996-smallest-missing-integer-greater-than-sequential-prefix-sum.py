class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        psum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                psum += nums[i]
            else:
                break
        
        while True:
            if psum not in nums:
                return psum
            else:
                psum += 1