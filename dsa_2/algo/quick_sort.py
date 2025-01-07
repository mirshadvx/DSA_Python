li =  [2, 5, 6 , 1 , 3 , 4]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [64, 25, 12, 22, 11]
sorted_numbers = quick_sort(li)
print(sorted_numbers)