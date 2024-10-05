def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if isinstance(arr[j], int) and isinstance(arr[j+1], int):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            if isinstance(arr[j], str) and isinstance(arr[j+1], str):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if isinstance(arr[j], int) and isinstance(arr[j+1], str):
                arr[j], arr[j+1] = arr[j+1], arr[j]

lista = ["daniele", 22, 30, 12, "Marc", "Eso", "Ulrich", 14, 17]
print("The default list is: ", (lista))

buble_sort(lista)
print("The ordered list is: ", (lista))
