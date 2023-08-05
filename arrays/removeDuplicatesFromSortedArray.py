# approach is to make ind pointer and run a loop till nums is not equal to its next and initialize it with the ind pointer so that 
# it will remove duplicates till ind and after that there are duplicates

def removeDuplicates(self, nums: List[int]) -> int:
      ind = 1
      for i in range(len(nums) - 1):
          if (nums[i] != nums[i + 1]):
              nums[ind] = nums[i + 1]
              ind += 1
      return ind
