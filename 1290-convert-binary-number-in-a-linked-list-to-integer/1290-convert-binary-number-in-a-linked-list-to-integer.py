# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        binary = ""
        while head != None:
            binary = binary + str(head.val)
            head = head.next
        
        num = int(binary,2)

        return num