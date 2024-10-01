# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data  # Características (sepal length, sepal width, petal length, petal width)
y = iris.target  # Clases (0, 1, 2 representando las especies)

# Dividir el conjunto de datos en entrenamiento y prueba (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo de Árbol de Decisión
arbol = DecisionTreeClassifier(random_state=42)

# Entrenar el modelo
arbol.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = arbol.predict(X_test)

# Evaluar la precisión del modelo
precision = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {precision * 100:.2f}%")

# Visualizar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(arbol, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True)
plt.show()

# Mostrar las características más importantes
importancias = arbol.feature_importances_
for nombre, importancia in zip(iris.feature_names, importancias):
    print(f'{nombre}: {importancia:.4f}')
