#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este 


INSTALAR DEPENDENCIAS

Ubuntu 16-4:
    sudo apt-get install python-tk
    sudo pip install matplotlib
    sudo pip install scipy
    sudo pip install sklearn
    sudo pip install pandas
"""


# Importar módulos necesarios
from sklearn import datasets
import matplotlib.pyplot as plt

# Cargue el conjunto de datos: digits (incluido en sklearn como ejemplo)
digits = datasets.load_digits()

# Imprima las claves y la descripción del conjunto de datos
print("Keys:")
print(digits.keys())
print("Description:")
print(digits.DESCR)

# Imprime la "shape" de las imágenes y las claves de datos
print("Images shape:")
print(digits.images.shape)
print("Data shape:")
print(digits.data.shape)
print("Target shape:")
print(digits.target.shape)

# # Mostrar dígito número: 123
# plt.imshow(digits.images[123], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()
# # Mostrar dígito número: 1010
# plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()
# # Mostrar dígito número: 1234
# plt.imshow(digits.images[1234], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()

# <>

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Crear matrices de "features" y de "target" desde el dataset "digits"
X = digits.data
y = digits.target

# # Custom data desde un archivo excel
# data_x = pd.read_excel("input.xlsx")
# X = data_x.as_matrix()
# y = pd.Series(range(0,len(X)))


# Dividir en el conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

n = 7 # número de "neighbors": knn

# Crea un clasificador k-NN con n neighbors: knn
knn = KNeighborsClassifier(n_neighbors=n)

# "Fit", cargar el clasificador a los datos de entrenamiento
knn.fit(X_train, y_train)

# Imprime la precisión
print("Accuracy ("+str(n)+"):")
print(knn.score(X_test, y_test))


neighbors = np.arange(1, 15)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

print "Test de diferentes valores de n_neighbors:"
kmem = 0
# Bucle sobre diferentes valores de k
for i, k in enumerate(neighbors):
    # Configure un clasificador k-NN con k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Ajustar el clasificador a los datos de entrenamiento
    knn.fit(X_train, y_train)
    
    # Computar la precisión en el conjunto de entrenamiento
    a = knn.score(X_train, y_train)

    # Compute la precisión en el conjunto de prueba
    b = knn.score(X_test, y_test)

    test_accuracy[i] = a
    train_accuracy[i] = b

    c = a-abs(a-b)
    if k>1 and kmem<c:
        print "\t",k,a-abs(a-b)
    kmem = c


# # Generar "plot" gráfica
# plt.title('k-NN: número variable de neighbors')
# plt.plot(neighbors, test_accuracy, label = 'Precisión de prueba')
# plt.plot(neighbors, train_accuracy, label = 'Precisión de entrenamiento')
# plt.legend()
# plt.xlabel('Number of Neighbors')
# plt.ylabel('Accuracy')
# plt.show()

#"""