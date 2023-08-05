# use the mathematics formula of n * (n + 1) // 2 for calculate sum of first n numbers
# then subtract the sum of array in O(n) time complexity.

def missingNumber(self, nums: List[int]) -> int:
    return ((len(nums) * (len(nums) + 1))// 2) - sum(nums)
