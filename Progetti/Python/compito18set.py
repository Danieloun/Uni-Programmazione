def means(arr):
    """
    input -> list(numeri)
    output -> nuova lista di numeri = m  // (m[i]) contenga 
            la media degli elementi in a[0:i+1]
    """

    m = []
    sum = 0
    for i, num in enumerate(arr):
        sum += num
        mean = sum / (i+1)
        m.append(mean)
    
    return m

lista = [1, 2, 3, 4, 5]
print("La lista iniziale è -> ", lista)
print("La lista 'm' è ugale a -> ", means(lista))