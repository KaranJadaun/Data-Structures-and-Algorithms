# xor has a property which cancels out it pair means 1 will cancel 1 one
# so if the array 1 1 1 so one 1 cancels another 1 and there is only one 1 left
# iterate in nums and eventually it will cancels out of duplicates and left with the single number 

def singleNumber(self, nums: List[int]) -> int:
    xor = 0
    for num in nums: xor ^= num
    return xor
