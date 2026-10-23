class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res = []
        l = head

        while head:
            res.append(head.val)
            head = head.next
        
        res[left-1:right] = res[left-1:right][::-1]

        head = l
        i = 0

        while head:
            head.val = res[i]
            i = i + 1
            head = head.next
        
        head = l

        return head