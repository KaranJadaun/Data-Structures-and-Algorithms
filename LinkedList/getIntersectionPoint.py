# take two pointers and iterate till the end if anyone of them reaches its end
# make the pointer go to the another ll because after one iteration it will be in same postion 
# from equal element and then return dummy1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummy1 = headA
        dummy2 = headB
        while dummy1 != dummy2:
            dummy1 = dummy1.next if dummy1 else headB
            dummy2 = dummy2.next if dummy2 else headA
        return dummy1
