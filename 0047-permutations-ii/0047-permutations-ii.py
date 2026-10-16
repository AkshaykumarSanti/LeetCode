class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        for num in nums:
            new = []

            for arr in res:
                for i in range(len(arr) + 1):
                    new.append(arr[:i] + [num] + arr[i:])
            
            res = new
        
        s = set()
        ans = []
        
        for arr in res:
            t = tuple(arr)
            if t not in s:
                s.add(t)
                ans.append(arr)
        
        return ans