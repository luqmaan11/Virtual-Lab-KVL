arr = [1,2,3,4,5,6]
n = len(arr)
i = 0
j = n - 1
l = []
k = 0
while i <= j:
    if k % 2 == 0:
        l.append(arr[j])
        j = j - 1
    else:
        l.append(arr[i])
        i = i + 1
    k = k + 1
print(l)