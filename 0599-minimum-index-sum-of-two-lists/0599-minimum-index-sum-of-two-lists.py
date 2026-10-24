class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        a = float("inf")
        for i in range(len(list1)):
            if list1[i] in list2:
                s = i + list2.index(list1[i])
                if len(res) == 0:
                    a = s
                    res.append(list1[i])
                else:
                    if s < a:
                        res.pop()
                        res.append(list1[i])
                        a = s
                    elif s == a:
                        res.append(list1[i])
        
        return res