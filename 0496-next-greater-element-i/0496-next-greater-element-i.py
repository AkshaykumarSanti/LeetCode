class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        i = 0
        for num in nums1:
            idx = nums2.index(num)
            for j in range(idx+1,len(nums2)):
                if nums2[j] > num:
                    res[i] = nums2[j]
                    break

            i = i + 1
        
        return res