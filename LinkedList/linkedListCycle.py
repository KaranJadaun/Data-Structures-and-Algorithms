# take two pointers fast and slow 
# it is obvious that if there is a cycle there has to be a point where both pointers meet
# so we check after each iteration if slow == fast and return directly from there

def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
