# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        res = []
        while curr != None:
            res.append(curr.val)
            curr = curr.next
        
        i = 0
        j = len(res) - 1
        ans = []

        while i <= j:
            ans.append(res[i])
            if i != j:
                ans.append(res[j])
            i = i + 1
            j = j - 1
        
        curr = head
        for i in ans:
            curr.val = i
            curr = curr .next
        
        return head