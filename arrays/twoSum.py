# take a hashmap and iterate if we find the difference of target - current num in hashmap then return it
# else initialize it with its index 
# this works on unsorted array as well as sorted array O(n) time and space
# use two pointers in case of sorted array O(n/2) time only 

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if (val in hashmap):
            return [i, hashmap[val]]
        hashmap[nums[i]] = i
