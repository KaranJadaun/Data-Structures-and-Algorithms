# take a slow and fast pointer. it is obvious that when fast will complete its iteration 
# slow will be at exact in middle of the linkedlist

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
