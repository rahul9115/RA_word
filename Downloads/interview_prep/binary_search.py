def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            print(arr[mid])
            print("Found the element")
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
arr=[1,1,1,2,2,2,3,3]
print(binary_search(arr,4))