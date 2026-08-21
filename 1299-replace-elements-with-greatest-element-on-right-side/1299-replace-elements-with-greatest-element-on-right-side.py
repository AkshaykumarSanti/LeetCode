class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        maxi = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = maxi

            if temp > maxi:
                maxi = temp

        return arr
        