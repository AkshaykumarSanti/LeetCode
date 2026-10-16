class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            new = []
            for arr in res:
                for i in range(len(arr) + 1):
                    new.append(arr[:i] + [num] + arr[i:])
            
            res = new
        
        return res