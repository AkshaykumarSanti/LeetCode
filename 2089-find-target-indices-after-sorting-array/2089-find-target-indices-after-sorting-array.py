class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        small = 0
        equal = 0
        for i in range(len(nums)):
            if nums[i] < target:
                small = small + 1
            elif nums[i] == target:
                equal = equal + 1
        
        res = []
        for i in range(small,small + equal):
            res.append(i)

        return res