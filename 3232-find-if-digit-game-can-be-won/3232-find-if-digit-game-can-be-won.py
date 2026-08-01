class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = 0
        a = 0
        for i in nums:
            if i < 10:
                s = s + i
            else:
                a = a + i
        if s > a or s < a:
            return True
        else:
            return False
        
        