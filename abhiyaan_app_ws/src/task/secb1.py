

temp = input().split()
m = int(temp[0])
n = int(temp[1])
k = int(input())
arr = []


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


def rowSelect(arr, x, l, r):
    if r >= l:
        mid = l+(r-l)//2
        if arr[mid][0] <= x and arr[mid+1][0] >= x:
            return mid
        elif arr[mid][0] > x:
            return rowSelect(arr, x, l, mid - x)
        else:
            return rowSelect(arr, x, mid + 1, r)


for i in range(m):
    arr.append([int(j) for j in input().split()])
row = rowSelect(arr, k, 0, m-1)
col = binarySearch(arr[row], 0, n-1, k)
if col == -1:
    print('False')
else:
    print('True')
    print(row, col)
