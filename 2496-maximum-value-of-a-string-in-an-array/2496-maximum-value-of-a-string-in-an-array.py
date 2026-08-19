class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = []
        for i in strs:
            if i.isdigit():
                res.append(int(i))
            else:
                res.append(len(i))
        
        return max(res)
        