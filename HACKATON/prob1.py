#Input -> Un inter n, ovvero il numero di secondi per cui la macchina
# di Gigino rimane accesa.
#OUTPUT -> Un intero x che rappresenta per quanti secondi Gigino 
#deve premere l'acceleratore per coprire la massima distanza possibile.


n = int(input("Tempo in cui la macchina rimane accesa: "))

if n % 2 == 1:
    n = n - 1

x = int(0)

x = n // 2
print("L acceleratore dovrà essere premuto ", x, "secondi per ricoprire la distanza maggiore")