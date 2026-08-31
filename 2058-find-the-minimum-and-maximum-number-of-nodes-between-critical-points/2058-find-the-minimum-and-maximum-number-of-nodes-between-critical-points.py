class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next

        res = []

        for i in range(1,len(nums)-1,1):
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                res.append(i+1)
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                res.append(i+1)

        res.sort()

        if len(res) < 2:
            return [-1,-1]
        
        mini = float("inf")
        for i in range(1,len(res)):
            if res[i] - res[i-1] < mini:
                mini = res[i] - res[i-1]
        
        maxi = res[-1] - res[0]

        return ([mini,maxi])
