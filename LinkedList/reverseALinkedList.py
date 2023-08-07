# simple approach is to take two pointer 
# at each iteration save temp and then make curr.next as prev 
# and then increment prev and curr to curr and temp respectively

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
