# take mini and maxi because to tackle negative numbers you have to use it because
# multipyling a negative number in both can swap their values so we have to keep it in our minds
# so whenever our nums get below zero we swap them
# them compare it multiplication with maxi and mini
# and then at last compare with answer

def maxProduct(self, nums: List[int]) -> int:
    maxi = nums[0]
    mini = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        if (nums[i] < 0):
            maxi, mini = mini, maxi
        maxi = max(nums[i], maxi * nums[i])
        mini = min(nums[i], mini * nums[i])
        ans = max(ans, maxi)
    return ans
