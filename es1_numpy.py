import numpy as np

#utilizzo la funzione arange per creare un array di numeri interi da 10 a 48
arr = np.arange(10, 49)
#verifico il tipo di dato dell'array e stampo il risultato
print("Tipo di dato iniziale", arr.dtype)
#cambio il tipo di dato in float64 e verifico il tipo di dato
arr = arr.astype(np.float64)
print("il tipo di dato dopo la conversione", arr.dtype)
#stampo la forma dell'array
print("Forma dell'array",arr.shape)

