# this is based on dutch flag algorithms 
# in this we will take three pointers for 0, 1 and 2
# and iterate till the last pointer crosses mid pointer
# when we get 0 we will swap the low and increment both
# if we get 1 then simply incremenet mid because its already at its place
# else if we get 2 then simply swap with high and decrement high pointer that it


def sortColors(self, nums: List[int]) -> None:
    low = 0
    mid = 0
    high = len(nums) - 1
    while (high >= mid):
        if (nums[mid] == 0):
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif (nums[mid] == 1):
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
