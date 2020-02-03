def selection(a, k):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a[k-1]
def selectionSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

data = [64, 25, 10, 22, 11]
selectionSort(data)
selection(data, 3)
print(data)
print(selection(data, 3))