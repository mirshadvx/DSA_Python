li =  [2, 5, 6 , 1 , 3 , 4]

for i in range(1, len(li)):
    j = i
    while j > 0 and li[j - 1] > li[j]:
        li[j - 1] , li[j] = li[j] , li[j - 1]
        j -= 1
        
print(li)
        