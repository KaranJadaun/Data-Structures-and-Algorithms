# take two pointers fast and slow 
# it is obvious that if there is a cycle there has to be a point where both pointers meet
# so we check after each iteration if slow == fast and return directly from there

# to check length of loop make slow = head and then again start its iterations with cnt++ variable
# if return the cnt variable when they meet again.


def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
