# take current cnt and maxi if there is one make cnt += 1 and compare with maxi
# else if it is 0 make cnt as 0 because it breaks the flow and return maxi

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    cnt = 0
    maxi = 0
    for num in nums:
        if (num == 1):
            cnt += 1
            maxi = max(maxi, cnt)
        else: 
            cnt = 0
    return maxi
