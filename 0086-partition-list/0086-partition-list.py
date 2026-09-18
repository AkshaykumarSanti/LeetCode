# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        
        nums = []
        for j in res:
            if j < x:
                nums.append(j)
        for j in res:
            if j >= x:
                nums.append(j)
        
        head = None
        root = None
        for i in nums:
            temp = ListNode(i)
            if root == None:
                root = temp
                head = temp
            else:
                root.next = temp
                root = root.next
        
        return head