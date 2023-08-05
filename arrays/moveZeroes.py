# iterate over the stack and whenever you see 0 remove it and append it to the end 

def moveZeroes(self, stack: List[int]) -> None:
    for num in stack:
        if num == 0:
            stack.remove(0)
            stack.append(0)
