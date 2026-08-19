class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        curr = dummy
        forw = dummy

        for _ in range(n + 1):
            forw = forw.next

        while forw:
            curr = curr.next
            forw = forw.next

        curr.next = curr.next.next

        return dummy.next