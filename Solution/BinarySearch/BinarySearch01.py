n = int(input())
array_n = list(map(int, input().split()))
m = int(input())
array_m = list(map(int, input().split()))

array_n.sort()
array_m.sort()

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start+end)//2

    if target == array[mid]:
        return True
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)


for i in array_m:
    if binary_search(array_n, i, 0, n) == True:
        print("yes", end=" ")
    elif binary_search(array_n, i, 0, n) == False:
        print("no", end=" ")
