# first make the nums sorted and then pop the first element and append in last so that the array is rotated by 1 place
# for each iteration check if it is equal

def check(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        if (sortedNums == nums): return True
        for i in range(len(nums)):
            a = nums.pop(0)
            nums.append(a)
            if (nums == sortedNums): return True
        return False
