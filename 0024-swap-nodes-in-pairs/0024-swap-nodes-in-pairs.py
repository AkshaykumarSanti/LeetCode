# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        res = []
        curr = head

        while curr:
            res.append(curr)
            curr = curr.next
        
        for i in range(0,len(res)-1,2):
            res[i],res[i+1] = res[i+1],res[i]
        
        for i in range(len(res)-1):
            res[i].next = res[i+1]
        
        res[-1].next = None

        return res[0]