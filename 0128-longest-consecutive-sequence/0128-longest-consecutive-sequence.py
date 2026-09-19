class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        max_count = 1
        count = 1
        last_smaller = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == last_smaller:
                continue
            elif nums[i] == last_smaller + 1:
                count += 1
            else:
                count = 1
                
            last_smaller = nums[i]
            
            if count > max_count:
                max_count = count
        
        return max_count