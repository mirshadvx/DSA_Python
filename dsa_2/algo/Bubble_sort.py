arr = [7, 3, 9, 12, 11]
length = len(arr)

for i in range(length):
    for j in range(length - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]
            
print(f"sorted array : {arr}")