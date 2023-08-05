# this is based on kadane's algo
# they say just add the ele to curr and compare it with maxi everything
# if curr goes zero that means subarray till ith index is not worth it to take so we make curr as 0
# at last return maxi

def maxSubArray(self, nums: List[int]) -> int:
    curr = 0
    maxi = nums[0]
    for num in nums:
        curr += num
        if (curr > maxi):
            maxi = curr
        if (curr < 0):
            curr = 0
    return maxi
