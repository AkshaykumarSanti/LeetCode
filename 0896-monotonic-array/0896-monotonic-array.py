class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        desc = True
        i = 0
        j = i + 1
        while j <= len(nums)-1:
            if nums[i] > nums[j]:
                inc = False
            if nums[i] < nums[j]:
                desc = False
            i = i + 1
            j = j + 1

        return inc or desc   