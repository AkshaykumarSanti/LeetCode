class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        if len(set(nums)) == 2:
            return len(nums)

        maxi = 0
        i = 0
        h = {}
        for k in range(len(nums)):
            if nums[k] in h:
                h[nums[k]] += 1
            else:
                h[nums[k]] = 1

            if len(h) > 2:
                h[nums[i]] -= 1
                if h[nums[i]] == 0:
                    del h[nums[i]]
                
                i = i + 1
            
            if k-i+1 > maxi:
                maxi = k-i+1

        return maxi