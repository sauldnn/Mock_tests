
len_sub   = len(arr)//2
pivot     = len(arr) - 1
left = 0
right = pivot
def Partition(left, right ,A):
    x = A[right]
    i = left-1
    for j in range(left, right):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i+1
def fin_median(arr, left, right, kth):
    while True:
        pivot_index = Partition(left, right, arr)
        len_n = pivot_index - left
        if kth == len_n:
            return arr[pivot_index]
            break
        elif kth<len_n:
            right = pivot_index-1
        else:
            kth = kth - len_n
            left = pivot_index + 1
        print(arr[pivot_index])


