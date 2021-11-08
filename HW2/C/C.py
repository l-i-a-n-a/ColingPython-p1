def solution(arr):
    arr1 = []
    while arr:
        arr1 += arr.pop(0)
        arr = list(zip(*arr))
        arr.reverse()
    return arr1