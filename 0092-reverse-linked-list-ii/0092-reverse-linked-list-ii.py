class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        
        res[left-1:right] = res[left-1:right][::-1]

        head = None
        root = None

        for i in res:
            temp = ListNode(i)
            if head == None:
                head = temp
                root = temp
            else:
                root.next = temp
                root = root.next 
        return head
        