class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        while l1 != None:
            a = str(l1.val) + a
            l1 = l1.next
        
        b = ""
        while l2 != None:
            b = str(l2.val) + b
            l2 = l2.next
        
        total = int(a) + int(b)

        if total == 0:
            return ListNode(0)

        head = None
        root = None
        while total != 0:
            r = total % 10
            total = total // 10
            temp = ListNode(r)
            if root == None:
                head = temp
                root = temp
            else:
                root.next = temp
                root = root.next
        
        return head