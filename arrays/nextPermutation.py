# this is mathematics based concept
# so first find the element which is just greater than its next 
# then make it temp and find element just greater than temp and swap them 
# reverse the element from temp + 1 index so it will become the next greater permutation of that number


def nextPermutation(self, nums: List[int]):
    def reverse(arr, start):
        end = len(arr) - 1
        while (start < end):
            arr[start], nums[end] = nums[end], arr[start]
            start += 1
            end -= 1
    i = len(nums) - 2
    while (i >= 0 and nums[i + 1] <= nums[i]):
        i -= 1
    temp = nums[i]
    if (i >= 0):
        j = len(nums) - 1
        while (temp >= nums[j]):
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    reverse(nums, i + 1)
