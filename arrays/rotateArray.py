# approach is to simply check if k is bigger than n 
# and simply do indexing in O(1) time and literally O(n) space complexity.

def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    nums[::] = nums[n - k:] + nums[:n - k]
