class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 1

        for i in range(len(nums)):
            prod = 1
            g = 0
            l = 1

            for j in range(i, len(nums)):
                x = nums[j]

                prod *= x
                g = math.gcd(g, x)
                l = l * x // math.gcd(l, x)

                if prod == g * l:
                    res = max(res, j - i + 1)

        return res