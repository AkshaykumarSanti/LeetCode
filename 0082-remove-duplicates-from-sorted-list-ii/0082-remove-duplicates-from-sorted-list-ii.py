# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = {}
        while head != None:
            if head.val in h:
                h[head.val] = h[head.val] + 1
            else:
                h[head.val] = 1
            head = head.next
        
        res = []
        for i in h:
            if h[i] == 1:
                res.append(i)
        
        head = None
        root = None

        for i in res:
            temp = ListNode(i)
            if root == None:
                root = temp
                head = temp
            else:
                root.next = temp
                root = root.next
        
        return head