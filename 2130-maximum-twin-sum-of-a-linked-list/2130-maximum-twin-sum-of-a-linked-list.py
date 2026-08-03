class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        
        psum = []
        i = 0
        j = len(a) - 1

        while i < j:
            psum.append(a[i]+a[j])
            i = i + 1
            j = j - 1
        
        return max(psum)   