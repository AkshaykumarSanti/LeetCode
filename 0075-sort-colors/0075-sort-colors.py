class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = len(nums) - 1
        mid = 0

        while mid <= j:
            if nums[mid] == 0:
                nums[mid],nums[i] = nums[i],nums[mid]
                mid = mid + 1
                i = i + 1
            elif nums[mid] == 1:
                mid = mid + 1
            else:
                nums[mid],nums[j] = nums[j],nums[mid]
                j = j - 1 
        
        return nums

        