class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        maxi = 0

        for i in arr:
            if i % 2 == 1:
                odd += 1
            else:
                odd = 0
            
            maxi = max(odd, maxi)
        
        return maxi >= 3