def BubbleSort(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i] #swap
    # return a

data = [55, 7, 78, 12, 42]
BubbleSort(data)
print(data)