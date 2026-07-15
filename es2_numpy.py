#slicing e f.indexing

#importo numpy
import numpy as np
#creo un array numpy 1d di 20 numeri interi casuali compresi tra 10 e 50
arr = np.random.randint(10, 51, 20)
#utilizzo lo slicing per estrarre i primi 10 elementi dell'array
s1 = arr[:10]
#utilizzo lo slicing per estrarre gli ultimi 5 elementi dell'array
s2 = arr[-5:]
#utilizzo lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso)
s3 = arr[5:15]
#utilizzo lo slicing per estrarre ogni terzo elemento dell'array
s4 = arr[::3]
#modifico tramite slicing gli elementi dall'indice 5 all'indice 10(escluso) assegnando loro il valore 99
arr[5:10] = 99
#stampo l'array originale e tutti quelli derivati dalle operazioni di slicing
print("array originale(modificato)", arr)
print("primi 10 elementi", s1)
print("ultimi 5 elementi", s2)
print("elementi dall'indice 5 all'indice 15", s3)
print("ogni terzo elemento", s4)
