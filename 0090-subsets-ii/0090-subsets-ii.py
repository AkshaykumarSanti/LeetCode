class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = [[]]

        for num in nums:
            size = len(res)
            for j in range(size):
                res.append(res[j]+[num])
        
        ans = []
        for sub in res:
            if sub not in ans:
                ans.append(sub)
        return ans

        