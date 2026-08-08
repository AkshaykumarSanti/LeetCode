class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans = True
        i = 1
        while ans:
            if i * k not in nums:
                ans = False
                return i * k
            else:
                i = i + 1

            

                

        