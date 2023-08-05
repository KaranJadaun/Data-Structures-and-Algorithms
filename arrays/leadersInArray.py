# this is simple just take maxi and if num is greater than maxi simple append it to leaders array

def printLeaders(arr, n):
    ans = []
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]
    return ans
