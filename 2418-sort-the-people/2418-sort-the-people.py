class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = {}
        for i in range(len(names)):
            h[heights[i]] = names[i]
        
        heights.sort(reverse=True)

        res = []
        for i in heights:
            res.append(h[i])

        return res 