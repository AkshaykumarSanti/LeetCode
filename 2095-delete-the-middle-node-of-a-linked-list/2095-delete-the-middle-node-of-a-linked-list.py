class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        len = 0
        
        while (head != None):
            a.append(head.val)
            len = len + 1
            head = head.next

        skip = len//2 + 1
        count = 0

        root = None
        head = None

        for i in a:
            count = count + 1
            if count == skip:
                continue
            temp = ListNode(i)
            if root == None:
                root = temp
                head = temp
            else:
                root.next = temp
                root = root.next
        return head
        
        