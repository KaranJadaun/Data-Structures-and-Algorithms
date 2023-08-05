# appraoch is to take a number and then check if its num + 1 is in nums or not and increment it by one and increase cnt if there is number
# and then just check if num - 1 is present that means that if will do the checking in another loop 
# check if it is not in nums, initialize cnt with 1 and make while loop and check for its num + 1 

def longestConsecutive(self, nums):
    nums = set(nums) 
    maxi = 0
    for i in nums:
        if (i - 1 not in nums): 
            num = i
            cnt = 1
            while (num + 1 in nums):
                cnt += 1
                num += 1
            maxi = max(maxi, cnt)
    return maxi
