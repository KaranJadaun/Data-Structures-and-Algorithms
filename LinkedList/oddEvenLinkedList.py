# take an odd and even pointer and evenHead to connect it at the end of iteration
# simply iterate and connect it after one place and move to them
# and at last simply connect odd one to evenHead and return

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head): return None
        odd = head
        even = head.next
        evenHead = even
        while (even and even.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
