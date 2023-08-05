# this is based on boyer moore voting algorithm
# approach to take cnt and check it is same as else then incremenet the cnt
# in between if cnt goes 0 it means it is not in majority and the last elements which stays in ele is the majority element

def majorityElement(self, nums: List[int]) -> int:
    ele = None
    cnt = 0
    for num in nums:
        if (cnt == 0):
            ele = num
        if (num == ele):
            cnt += 1
        else:
            cnt -= 1
    return ele
