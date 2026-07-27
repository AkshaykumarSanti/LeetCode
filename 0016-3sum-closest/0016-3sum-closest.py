class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(close - target):
                    close = s

                if s < target:
                    j = j + 1
                elif s > target:
                    k = k - 1
                else:
                    return s
        return close
                
                        
        