# most efficient approach is using slow fast
# firstly iterate fast to the nth position and connext the last node to head if not fast
# then iteratte them to the last and connect slow to slow.next.next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = head
    fast = head
    for i in range(n):
        fast = fast.next
    if (not fast): return head.next
    while (fast.next):
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
