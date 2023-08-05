# simply iterate over the array and check with target 

def linearSearch(nums, target):
  for num in nums:
    if (num == target):
      return True
  return False
