# approach is to first sort based on 0th index of each element in 2d matrix
# if res is empty append the element and if first element is greater than res's last element then append
# and then if first element is smaller then res's last element then take the max of second element of interval and res's last element

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = []
    for interval in intervals:
        if (not res or interval[0] > res[-1][1]):
            res.append(interval)
        elif (interval[0] <= res[-1][1]):
            res[-1][1] = max(interval[1], res[-1][1])
    return res
