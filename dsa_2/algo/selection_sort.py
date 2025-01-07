li = [64, 34, 25, 5, 22, 11, 90, 12]

for i in range(len(li) - 1):
    min_index = i
    for j in range(i + 1, len(li)):
        if li[j] < li[min_index]:
            min_index = j
    li[i] , li[min_index] = li[min_index], li[i]
    
print(li)