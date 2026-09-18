# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        a = []
        while l1 != None:
            a.append(l1.val)
            l1 = l1.next
        
        b = []
        while l2 != None:
            b.append(l2.val)
            l2 = l2.next
        
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            x = a[i] if i >= 0 else 0
            y = b[j] if j >= 0 else 0

            total = x + y + carry
            ans.append(total % 10)
            carry = total // 10

            i = i - 1
            j = j - 1
        
        ans.reverse()

        head = None
        root = None

        for i in ans:
            temp = ListNode(i)
            if root == None:
                root = temp
                head = temp
            else:
                root.next = temp
                root = root.next
        
        return head