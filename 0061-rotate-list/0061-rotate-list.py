class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        arr = []

        while head != None:
            arr.append(head.val)
            head = head.next

        r = k % len(arr)
        a = arr[len(arr)-r: ] + arr[:len(arr)-r]
        head = None
        root = None

        for i in a:
            temp = ListNode(i)
            if head == None:
                head = temp
                root = temp
            else:
                root.next = temp
                root = root.next
        
        return head

        