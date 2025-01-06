def binary(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid -1
            
    return -1



arr = [1, 3, 5, 7, 9, 11, 13, 15]
res = binary(arr, 9)

if res == -1:
    print("element not found")
else:
    print(f"element found in position {res}")